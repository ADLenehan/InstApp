from django.db import models

# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=30)
    parent_category = models.IntegerField()

class Handles (models.Model):
    handle = models.CharField(max_length=30)
    category = models.ForeignKey(Categories)