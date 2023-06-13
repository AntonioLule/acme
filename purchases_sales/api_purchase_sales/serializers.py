# Rest Framework
from rest_framework import serializers

# Models
from purchases_sales.models import *

class ProductSerializer(serializers.ModelSerializer):
    initial_balance = serializers.ReadOnlyField(source='store_usr.initial_balance')

    class Meta:
        model = Products
        fields = '__all__'