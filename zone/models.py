from django.db import models

# Create your models here.
class info(models.Model):
 frist_name=models.CharField( max_length=50)
 last_name=models.CharField( max_length=50)
 email=models.EmailField( max_length=254)
 serial=models.IntegerField()
 password=models.CharField( max_length=50)
 repassword=models.CharField( max_length=50)
 text=models.CharField( max_length=50)
 chackbox=models.CharField( max_length=50)
 payment=models.IntegerField()
 django=models.CharField( max_length=50)
