from django.urls import path
from .views import UserNetView,UserNetPublicView

urlpatterns = [
    path('profile/<int:pk>/', UserNetView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('<int:pk>/', UserNetPublicView.as_view({'get': 'retrieve'})),
]
