# Rest Framework
from rest_framework import serializers

# Models
from purchases_sales.models import *

class ProductSerializer(serializers.ModelSerializer):
    initial_balance = serializers.ReadOnlyField(source='store_usr.initial_balance')
    quantity = serializers.IntegerField(read_only=True)
    type_operation = serializers.CharField(read_only=True)
    store_usr = serializers.IntegerField(read_only=True)

    class Meta:
        model = Products
        fields = ('name', 'description', 'price', 'category', 'initial_balance', 'quantity', 'type_operation', 'store_usr')

    def validate_name(self, value):
        # Verificar si ya existe otro objeto con el mismo nombre
        exist_object = Products.objects.filter(name=value).first()
        if exist_object:

            return exist_object

        return value