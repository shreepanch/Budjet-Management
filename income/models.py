from django.db import models
from category.models import Category
from expenses.models import Expenses
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
def isPositive(value):
    if value<0:
        raise ValidationError("value must be greater than 0 or in positive number")

class Income(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(null=True,blank=True)
    date = models.DateField(default=timezone.now)
    rupes = models.FloatField(validators=[isPositive])
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


