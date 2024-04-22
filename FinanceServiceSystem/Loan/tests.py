from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import Provider, Consumer, ProviderLoan, ConsumerLoan

class ProviderLoanTestCase(TestCase):
    def setUp(self):
        self.provider = Provider.objects.create(name="Provider 1", email="provider@example.com", slug="provider-1")
    
    def test_add_loan(self):
        loan = ProviderLoan.objects.create(name="Loan 1", amount=1000, loan_term=12, InterestRateForProvider=0.21, Provider=self.provider)
        self.assertEqual(loan._Interest_amount,210)  # Assuming the interest amount is correctly calculated
    
    def test_view_method(self):
        loan = ProviderLoan.objects.create(name="Loan 1", amount=1000, loan_term=12, InterestRateForProvider=0.21, Provider=self.provider)
        self.assertEqual(loan.View(), "/loan-1/")
        
class ConsumerLoanTestCase(TestCase):
    def setUp(self):
        self.consumer = Consumer.objects.create(name="Consumer 1", email="consumer@example.com", slug="consumer-1")
    
    def test_add_loan(self):
        loan = ConsumerLoan.objects.create(name="Loan 1", amount=1000, loan_term=12, InterestRateForConsumer=0.24, consumer=self.consumer)
        self.assertEqual(loan._Interest_amount, 20)  
    def test_pay_method(self):
        loan = ConsumerLoan.objects.create(name="Loan 1", amount=1000, loan_term=12, InterestRateForConsumer=0.24, consumer=self.consumer)
        loan.Pay(20)
        self.assertEqual(loan._payment, 1)

