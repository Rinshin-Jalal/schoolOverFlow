from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/password_reset/',
         include('django_rest_passwordreset.urls', namespace='password_reset')),

    path('auth/', include('authentication.urls'))
]
