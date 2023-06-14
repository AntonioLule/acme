#Django
from django.db import transaction
#Rest
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import ValidationError
from rest_framework.authentication import TokenAuthentication

# Models
from purchases_sales.models import *
from .serializers import ProductSerializer


class ResultsSetPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 50


class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ResultsSetPagination

    def list(self, request, *args, **kwargs):

        user_id = kwargs.get('user_id')
        queryset = self.filter_queryset(self.get_queryset())

        # Obtener el valor de initial_balance para el usuario actual
        try:
            user = Store_Usr.objects.get(pk=user_id)
        except:
            user = None
        
        initial_balance = None
        if user:
            initial_balance = user.initial_balance

        # Paginar los resultados
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = serializer.data
            for item in data:
                item['initial_balance'] = initial_balance
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        for item in data:
            item['initial_balance'] = initial_balance

        return Response(data)

    @transaction.atomic()
    def create(self, request, *args, **kwargs):

        # Llamar al método create() del padre para crear el objeto BuySell
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            # Obtener el objeto guardado
            object_products = serializer.instance

            quantity = request.data.get('quantity')
            price = request.data.get('price')
            type_operation = request.data.get('type_operation')
            usr = request.data.get('store_usr')

            try:
                object_user = Store_Usr.objects.get(pk=usr)

                rst = quantity * price
                object_balance = object_user.initial_balance

                if type_operation == 'BUY' and rst <= object_user.initial_balance:
                    value_balance = rst - object_balance
                    object_user.initial_balance = value_balance
                    object_user.save()

                elif type_operation == 'SALE':
                    value_balance = rst + object_balance
                    object_user.initial_balance = value_balance
                    object_user.save()
                else:
                    raise ValidationError('No tienes fondos suficientes para generar esta operacion')
            except:
                object_user = None

            try:
                # Guardo o actualizo existencias
                try:
                    exist_object = Existence.objects.get(products=object_products.pk)
                    quantity_total = exist_object.quantity + quantity
                    exist_object.quantity = quantity_total
                    exist_object.save()
                except:
                    existence_object = Existence(
                        quantity=quantity,
                        products=object_products
                    )
                    existence_object.save()

                # Registro de la operación
                object_buy_sell = BuySell(
                price=price,
                type_operation=type_operation,
                quantity=quantity,
                products=object_products,
                store_usr=object_user
                )
                object_buy_sell.save()

            except Exception as err:
                raise ValidationError(err)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @transaction.atomic()
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        # Aquí puedes realizar acciones adicionales después de la actualización
        # Puedes acceder a los datos actualizados a través de serializer.data
        
        return Response(serializer.data)