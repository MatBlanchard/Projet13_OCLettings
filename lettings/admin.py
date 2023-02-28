from django.contrib import admin
from lettings.models import Letting, Address

class AdressAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'number']

admin.site.register(Letting)
admin.site.register(Address, AdressAdmin)
