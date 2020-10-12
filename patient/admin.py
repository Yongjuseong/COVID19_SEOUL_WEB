from django.contrib import admin
from django.contrib import admin
from patient.models import Patient_TBL

# Register your models here.
@admin.register(Patient_TBL)
class Patient_TBLAdmin(admin.ModelAdmin):
    list_display = ('id','name','pnumber','status') # admin에서 보여주는 항목

