from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class MyUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, null=False)
    year = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2020)])
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
