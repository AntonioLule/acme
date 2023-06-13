from django.urls import include, path
from rest_framework import routers
from .views import ProductViewSet

app_name = 'api_sales'

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]