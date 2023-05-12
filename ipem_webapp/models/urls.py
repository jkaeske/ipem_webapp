from django.urls import path

from .views import (
    development_activity_detail_view,
    model_description_detail_view,
    model_detail_view,
    model_table_view,
    problem_solving_activity_detail_view,
)

app_name = "models"

urlpatterns = [
    path("", model_table_view, name="model_table"),
    path(
        "<int:pk>/description/",
        model_description_detail_view,
        name="model_description_detail",
    ),
    path("<int:pk>/<str:layer>/", model_detail_view, name="model_detail"),
    path(
        "development_activities/<int:pk>",
        development_activity_detail_view,
        name="development_activity_detail",
    ),
    path(
        "<int:pk>/<str:layer>/development_activities/<int:activity_pk>/<str:spalten>",
        problem_solving_activity_detail_view,
        name="problem_solving_activity_detail",
    ),
]
