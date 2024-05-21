from django.db import models

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=32, null=False)

    def __str__(self) -> str:
        return f"{self.tag}"

class Quote(models.Model):
    description = models.CharField(max_length=256, null=False)
    author = models.CharField(max_length=64, null=False)
    tags = models.ManyToManyField(Tag)

