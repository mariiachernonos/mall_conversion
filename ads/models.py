from django.db import models

CATEGORY_CHOICES = (
    ('food', 'Food'),
    ('clothes', 'Clothes'),
    ('transport', 'Transport'),
    ('health', 'Health'),
    ('entertainment', 'Entertainment'),
    ('luxury', 'Luxury lifestyle'),
    ('cosmetics', 'Cosmetics'),
    ('electronics', 'Electronics')
)


class Ad(models.Model):
    codename = models.CharField(max_length=120)
    brand = models.CharField(max_length=40)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=30)

    def __str__(self):
        return f"{self.codename} {self.brand} {self.category}"
