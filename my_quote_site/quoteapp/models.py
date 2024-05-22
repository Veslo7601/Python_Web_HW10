from django.db import models

# Create your models here.

class Autors(models.Model):
    name = models.CharField(max_length=32, null=False, unique=True)
    born_date = models.CharField(max_length=32, null=False)
    born_location = models.CharField(max_length=64, null=False)
    description = models.CharField(max_length=256, null=False)

    def __str__(self):
        return f"{self.name}"

class Tag(models.Model):
    name = models.CharField(max_length=25, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"

class Quotes(models.Model):
    tags =  models.ManyToManyField(Tag)
    author = models.ForeignKey(Autors, on_delete=models.CASCADE)
    quote = models.CharField(max_length=126, null=False)
