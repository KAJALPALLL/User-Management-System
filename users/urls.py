from django.urls import path
from .views import UserAPIView

urlpatterns = [
    path('users', UserAPIView.as_view()),
    path('users/<str:pk>', UserAPIView.as_view()),
]