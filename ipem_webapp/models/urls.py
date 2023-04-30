from django.urls import path

from .views import model_detail_view, model_table_view

app_name = "models"

urlpatterns = [
    path("", model_table_view, name="model_table"),
    path("<int:pk>/<str:layer>/", model_detail_view, name="model_detail"),
]
