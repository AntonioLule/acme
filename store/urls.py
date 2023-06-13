from django.urls import include, path
from django.conf.urls import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import logout_then_login, LoginView

from purchases_sales.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('logout/', logout_then_login, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('home/', HomeView.as_view(), name='home'),

    # API
    path('api/', include('purchases_sales.api_purchase_sales.urls', namespace='api_sales')),

]

"""if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

    urlpatterns += static(settings.UPLOAD_URL, document_root=settings.UPLOAD_ROOT)
"""