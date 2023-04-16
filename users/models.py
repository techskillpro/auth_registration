from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 225, null = False)
    phone_number = models.CharField(max_length = 100, null = False)
    email = models.EmailField(null=False)
    # address = models.CharField(max_length = 255)
    
    class Meta:
        db_table = "Contact Information"

    def __str__(self):
        return self.name