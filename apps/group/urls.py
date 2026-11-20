from django.urls import path
from . import views

urlpatterns = [
    path("", views.GroupListCreateAPIView.as_view()),
    path("<int:pk>/", views.GroupDetailAPIView.as_view()),
]