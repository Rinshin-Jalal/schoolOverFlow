from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('su/', views.SignUp.as_view()),
    path('si/token/access/', TokenRefreshView.as_view(), name='token_get_access'),
    path('si/token/both/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('verify/email/', views.EmailVerifyView.as_view(), name="verify_email"),

]
