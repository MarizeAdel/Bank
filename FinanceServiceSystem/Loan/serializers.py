from rest_framework import serializers
from .models import user,Provider,Consumer, Loans,ConsumerLoan,ProviderLoan
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['name', 'email', 'slug']

class ProviderSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Provider

class ConsumerSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Consumer

class LoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = ['name', '_Interest_amount', 'amount', 'loan_term', 'date_added', 'slug']

class ProviderLoanSerializer(LoansSerializer):
    class Meta(LoansSerializer.Meta):
        model = ProviderLoan
        fields = LoansSerializer.Meta.fields + ['InterestRateForProvider', 'Provider']
        

class ConsumerLoanSerializer(LoansSerializer):
    class Meta(LoansSerializer.Meta):
        model = ConsumerLoan
        fields = "__all__"
        
        
