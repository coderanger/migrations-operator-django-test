from django.db import models

class TestModel(models.Model):
    col_one = models.CharField(max_length=200)
