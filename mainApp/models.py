from django.db import models

# Create your models here.
class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=10)
    dsg=models.CharField(max_length=20)
    salary=models.IntegerField()
    city=models.CharField(max_length=20, null=True, default=" ",blank=True)
    state=models.CharField(max_length=20, null=True, default=" ",blank=True )

    def __str__(self):
        return str(self.id) +"/"+ self.name +"/"+self.email

