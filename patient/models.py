from django.db import models

# Create your models here.
class Patient_TBL(models.Model):
    name=models.CharField('NAME',max_length=100,blank=False) #이름
    pnumber = models.CharField('NUMBER',max_length=50,blank=False) # Phone_number
    email = models.CharField('EMAIL', max_length=50, blank=False) # Email 주소
    status = models.CharField('STATUS', max_length=50, blank=False) #환자 상태
    hospital_dt = models.DateTimeField('HOSPITALIZATION_DATE') #입원날짜
    address = models.CharField('ADDRESS', max_length=50, blank=False) #주소
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id','name','status','hospital_dt')

