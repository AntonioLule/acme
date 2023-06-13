from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

# Models
from purchases_sales.models import *
from .serializers import ProductSerializer


class ResultsSetPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ResultsSetPagination

    def create(self, request, *args, **kwargs):
        # Realizar acciones adicionales antes de crear el objeto BuySell
        # Puedes acceder a los datos de la solicitud a través de request.data
        # Realizar validaciones o ejecutar lógica personalizada aquí

        # Llamar al método create() del padre para crear el objeto BuySell
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)

        # Realizar acciones adicionales después de crear el objeto BuySell
        # Puedes acceder al objeto recién creado a través de serializer.instance
        # Realizar cualquier acción adicional necesaria aquí

        return Response(serializer.data, status=status.HTTP_201_CREATED)