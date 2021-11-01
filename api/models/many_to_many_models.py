from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(db_index=True, default=timezone.now)

    class Meta:
        abstract = True


class Topping(BaseModel):
    pass

    def __str__(self):
        return self.name


class Pizza(BaseModel):
    toppings = models.ManyToManyField(Topping, related_name='pizza', blank=True)

    def __str__(self):
        return self.name
