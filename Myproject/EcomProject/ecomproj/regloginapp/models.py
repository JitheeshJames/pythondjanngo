from django.db import models

# Create your models here.

class SignUp(models.Model):
    firstname = models.CharField(max_length=100,blank=True)
    lastname = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    mobile = models.CharField(max_length=11)
    profile_pic = models.ImageField(upload_to='profilepic')
    passw = models.CharField(max_length=100)


    def __str__(self):
        return '{}'.format(self.email)

