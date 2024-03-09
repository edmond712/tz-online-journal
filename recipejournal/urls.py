from django.contrib import admin
from django.urls import path, include
from app import urls
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
