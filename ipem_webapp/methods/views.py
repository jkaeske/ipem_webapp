from django.views.generic import DetailView
from django_tables2 import SingleTableView

from .models import Method
from .tables import MethodTable


class MethodTableView(SingleTableView):
    model = Method
    table_class = MethodTable
    template_name = "pages/method_list.html"


method_table_view = MethodTableView.as_view()


class MethodDetailView(DetailView):
    template_name = "pages/method_abstract.html"
    context_object_name = "method"

    def get_queryset(self):
        return Method.objects.filter(pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view"] = self.kwargs["view"]

        return context


class ModelDetailView(DetailView):
    template_name = "pages/model.html"
    context_object_name = "model"

    def get_queryset(self):
        return Method.objects.filter(pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view"] = self.kwargs["view"]

        return context


method_detail_view = MethodDetailView.as_view()
