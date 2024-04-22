from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

total_amount_from_providers = 0
total_amount_to_consumers = 0
#creating user as base class 
class user(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField()
    slug = models.SlugField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/{self.slug}/'

#creating a Provider and consumer classes that inherite from user 
class Provider(user):
   pass


class Consumer(user):
    pass


#creating loan class as base class  

class Loans(models.Model):
    name = models.CharField(max_length=100)
    _Interest_amount=models.DecimalField(max_digits=10,decimal_places=2)
    amount=models.DecimalField(max_digits=12, decimal_places=2)
    loan_term = models.IntegerField()  # Representing the term in months for example assume it is one year
    date_added=models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
#creating Provideloan and Consumerloan classes that inherite from loans class  

class ProviderLoan(Loans):
    
    INTEREST_RATE_CHOICES = (
        (Decimal('0.21'), '21%'),
        (Decimal('0.22'), '22%'),
        (Decimal('0.23'), '23%'),
    )
    InterestRateForProvider=models.DecimalField(max_digits=10, 
                                                decimal_places=5,
                                                choices=INTEREST_RATE_CHOICES)
    Provider = models.ForeignKey(Provider,on_delete=models.PROTECT)
    def CalculateInterest(amount,InterestRateForProvider,loan_term):
        return (amount*InterestRateForProvider)/loan_term
        
    def AddLoan(self,n,am,InterestRate,_term):
        self._Interest_amount=(am*InterestRate)/_term
        self.name=n
        self.amount=am
        self.InterestRateForProvider=InterestRate
        self.loan_term=_term
        total_amount_from_providers+=am
        self.save()
        return True
    def View(self):
        return self.get_absolute_url()
    def save(self, *args, **kwargs):
        if not self._Interest_amount:
            self._Interest_amount= (self.amount*self.InterestRateForProvider)/self.loan_term
        super().save(*args, **kwargs)



class ConsumerLoan(Loans):
    _payment = models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(12)])
    INTEREST_RATE_CHOICES = (
        (Decimal('0.24'), '24%'),
        (Decimal('0.25'), '25%'),
        (Decimal('0.26'), '26%'),
    )
    InterestRateForConsumer=models.DecimalField(max_digits=5,
                                                 decimal_places=2,
                                                 choices=INTEREST_RATE_CHOICES)
    consumer = models.ForeignKey(Consumer,on_delete=models.PROTECT)
    def CalculateInterest(amount,InterestRate,_term):
        return (amount * (1 + InterestRate)**_term)/12
        
    def AddLoan(self,n,am,InterestRate,_term):
        if(total_amount_from_providers>total_amount_to_consumers and total_amount_from_providers>0 ):
            self._Interest_amount=((am*InterestRate)**_term)/12
            self.name=n
            self.amount=am
            self.InterestRateForProvider=InterestRate
            self.loan_term=_term
            total_amount_to_consumers+=am
            self.save()
            return True
        else:
            return False
        
        
    def Pay(self,arg):
        if arg==self._Interest_amount and self._payment<=12:
            self._payment+=1
            return True
        else:
            return False
    def save(self, *args, **kwargs):
        if not self._Interest_amount:
            self._Interest_amount= (self.amount * (1 + self.InterestRateForConsumer)**self.loan_term)/12
        super().save(*args, **kwargs)
   