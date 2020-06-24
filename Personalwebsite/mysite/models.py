from django.db import models

# Create your models here.
class student(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=210)

    def __str__(self):
        return self.firstname

class contact(models.Model):
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.email

