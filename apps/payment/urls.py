from django.urls import path
from . import views

urlpatterns = [
    path("", views.PaymentListCreateAPIView.as_view()),
    path("<int:pk>/", views.PaymentDetailAPIView.as_view()),
]