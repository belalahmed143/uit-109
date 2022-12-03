from django.db import models

# Create your models here.
class Department(models.Model):
    name  = models.CharField(max_length = 150)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.PositiveIntegerField()
    image = models.ImageField(upload_to='StudentImage')
    department  = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    
    
    def __str__(self):
        return self.name



class Teacher(models.Model):
    name  = models.CharField(max_length = 150)
    designation  = models.CharField(max_length = 150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['?']

class Contact(models.Model):
    name = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 150)
    email = models.EmailField()
    subject  = models.CharField(max_length = 150)
    message  = models.TextField()

    def __str__(self):
        return self.phone

class NewsLetter(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email
    






    
