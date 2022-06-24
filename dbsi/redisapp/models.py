from statistics import mode
from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class EmployeeDetail(models.Model):
    category = models.ForeignKey(Employee,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name