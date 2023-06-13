from django.db import models

#Enums
from utils.enums import Category, TypeOperation

#Models
from utils.models import BaseModelName, BaseModelQuantity
from django.contrib.auth.models import AbstractUser


class Store_Usr(AbstractUser):
    # Agrega tus campos personalizados aquí
    initial_balance = models.DecimalField(default=1000, null=True, blank=True, max_digits=20, decimal_places=2) #Saldo inicial
    
    def __str__(self):
        return self.username


class Products(BaseModelName):

    description = models.TextField(null=True, blank=True)  # Descripción
    price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)  # Precio
    # Categoria ENUM
    category = models.CharField(max_length=35, null=True, blank=True,
                                      choices=[(tag.name, tag.value) for tag in Category], default=Category.GROCERY.name)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class Existence(BaseModelQuantity):
    """
    Existencias
    """
    # Llaves foraneas
    products = models.ForeignKey(Products, null=True, blank=True, on_delete=models.SET_NULL)


class BuySell(BaseModelQuantity):

    price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)  # Precio

    # Tipo de operación ENUM
    type_operation = models.CharField(max_length=35, null=True, blank=True,
                                      choices=[(tag.name, tag.value) for tag in TypeOperation])

    # Llaves foraneas
    store_usr = models.ForeignKey(Store_Usr, null=True, blank=True, on_delete=models.SET_NULL)
    products = models.ForeignKey(Products, null=True, blank=True, on_delete=models.SET_NULL)