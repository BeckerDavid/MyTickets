from django.contrib import admin
from .models import *


# Register your models here.


class CountryAdmin(admin.ModelAdmin): pass


class CompanyAdmin(admin.ModelAdmin): pass


    # list_filter = ( 'actors__last_name', )


class PersonAdmin(admin.ModelAdmin): pass


class TicketAdmin(admin.ModelAdmin): pass


admin.site.register(Country, CountryAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Ticket, TicketAdmin)
