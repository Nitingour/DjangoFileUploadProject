from django.db import models

from django.db import models
from django.forms import ModelForm

class Upload(models.Model):
    name=models.CharField(max_length=30)
    pic=models.FileField(upload_to='images/')
    upload_date=models.DateTimeField(auto_now_add=True)
