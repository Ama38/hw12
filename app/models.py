from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    count_on_stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Client(models.Model):
    name = models.CharField(max_length=150)
    order = models.ManyToManyField(Product)

