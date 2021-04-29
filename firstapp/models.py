from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}, {self.name}'


owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
highlited = models.Field
