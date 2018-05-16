from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.name
