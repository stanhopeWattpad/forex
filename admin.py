from django.contrib import admin
from forex.models import Currency, CurrencyPrices

class CurrencyAdmin(admin.ModelAdmin): 
    search_fields=["name", ]
    list_display = ('name', 'symbol', 'digits', 'num_code', 'ascii_symbol')
admin.site.register(Currency, CurrencyAdmin)

class CurrencyPricesAdmin(admin.ModelAdmin): 
    search_fields=["name", ]
    list_filter=['currency']
admin.site.register(CurrencyPrices, CurrencyPricesAdmin)


