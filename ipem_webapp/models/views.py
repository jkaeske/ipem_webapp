from django.views.generic import DetailView
from django_tables2 import SingleTableView

from .models import Model
from .tables import ModelTable


class ModelDetailView(DetailView):
    template_name = "pages/model.html"
    context_object_name = "model"

    def get_queryset(self):
        return Model.objects.prefetch_related("layer").filter(pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["layer_name"] = self.kwargs["layer"]
        context["layer"] = self.object.layer.first()
        context["activity_count"] = context["layer"].development_activity.all().count()
        print(context["layer"])
        print(context["layer_name"])
        print(context["activity_count"])

        return context


model_detail_view = ModelDetailView.as_view()


class ModelTableView(SingleTableView):
    model = Model
    table_class = ModelTable
    template_name = "pages/model_list.html"


model_table_view = ModelTableView.as_view()
