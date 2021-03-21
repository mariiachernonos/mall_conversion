from django.db import models

from django.db import models

CATEGORY_CHOICES = (
    ('food', 'Food'),
    ('clothes', 'Clothes'),
    ('transport', 'Transport'),
    ('health', 'Health'),
    ('entertainment', 'Entertainment'),
    ('luxury', 'Luxury lifestyle'),
    ('cosmetics', 'Cosmetics'),
)


class Ad(models.Model):
    id = models.AutoField()
    codename = models.CharField(max_length=120)
    brand = models.CharField(max_length=40)
    category = models.CharField(choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.codename} {self.brand} {self.category}"

