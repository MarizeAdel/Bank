from django.contrib import admin
from .models import Provider,Consumer,ProviderLoan,ConsumerLoan
# Register your models here.
admin.site.register(Provider)
admin.site.register(Consumer)

class ProviderLoanAdmin(admin.ModelAdmin):
    exclude = ('_Interest_amount',)  # Exclude the Interest_amount field

# Register the ProviderLoan model with the custom admin class
admin.site.register(ProviderLoan, ProviderLoanAdmin)


class ConsumerLoanAdmin(admin.ModelAdmin):
    exclude = ('_Interest_amount','_payment')  # Exclude the Interest_amount field and payment

# Register the ProviderLoan model with the custom admin class
admin.site.register(ConsumerLoan, ConsumerLoanAdmin)
