from django.db import models

# Create your models here.
class Register(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phoneno=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    aadhar=models.CharField(max_length=100)
    password1=models.CharField(max_length=100)
    #password2=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    class Meta:
        db_table="users"

class Image(models.Model): 
    caption=models.CharField(max_length=100) 
    image=models.ImageField(upload_to="img/%y") 
    def __str__(self): 
        return self.caption 
# Create your models here.
