from django.db import models

class BaseModelName(models.Model):
    """
    Establecemos la base para los modelos con nombre y fechas
    """

    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class BaseModelQuantity(models.Model):
    """
    Establecemos la base para los modelos con cantidad y fechas
    """

    quantity = models.FloatField(default=0, null=True, blank=True)  # Cantidad
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True