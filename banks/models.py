from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bank(models.Model):
    
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class BankStatement(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    file = models.FileField(upload_to='statements/')
    upload_at = models.DateTimeField(auto_now_add=True)
    month = models.DateField()
    format = models.CharField(max_length=10, 
                              choices=[('pdf', 'PDF'), ('csv', 'CSV')])
    
    