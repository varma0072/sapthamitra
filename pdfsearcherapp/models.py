from django.db import models

# Create your models here.

class subjects(models.Model):
    Name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images')
    subjectcode=models.CharField(max_length=10)

    def __str__(self):
        return self.subjectcode

class pdfmodel(models.Model):
    Name=models.CharField(max_length=50)
    subjectcode=models.CharField(max_length=10)
    pdffile=models.FileField(upload_to='pdfs')
    
    def __str__(self):
        return self.Name
