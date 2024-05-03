from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'


class Computers(models.Model):
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    make = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        db_table = 'computers'


    def __str__(self):
        return f'{self.model} - {self.price}'

# Create your models here.
