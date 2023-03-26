from django.urls import path

from .views import method_detail_view, method_table_view

app_name = "methods"

urlpatterns = [
    path("", method_table_view, name="method_table"),
    path("<int:pk>/<str:view>/", method_detail_view, name="method_detail"),
]
