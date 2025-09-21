from django.contrib import admin
from .models import Destination

# Register your models here.

admin.site.site_header = "Booking Admin"
admin.site.register(Destination)

class Destination(admin.ModelAdmin):
    list_display = ('city', 'country', 'statustype')
    list_filter = ('statustype')
    search_fields = ('city', 'country')

