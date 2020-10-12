from django.contrib import admin
from agency.models import Agency


# Register your models here.
@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')

