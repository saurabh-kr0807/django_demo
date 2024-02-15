from django.urls import path
from .views import CustomerView

urlpatterns = [
    path('customers/', CustomerView.as_view()),
    path('customers/<int:pk>/', CustomerView.as_view()),
    path('customers/<int:pk>/update/', CustomerView.as_view()),
    path('customers/<int:pk>/delete/', CustomerView.as_view())
]
