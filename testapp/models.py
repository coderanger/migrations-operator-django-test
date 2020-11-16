from django.db import models

class TestModel(models.Model):
    col_one = models.CharField(max_length=200)
    col_two = models.CharField(max_length=200, default='')
