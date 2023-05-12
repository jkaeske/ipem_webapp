from django.views.generic import DetailView
from django_tables2 import SingleTableView

from ipem_webapp.methods.tables import MethodTableSimple

from .models import DevelopmentActivity, Model
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
        context["development_activity"] = DevelopmentActivity.objects.filter(
            layer=context["layer"]
        ).order_by("order")
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

    def get_queryset(self):
        return Model.objects.filter(is_public=True)


model_table_view = ModelTableView.as_view()


class ModelDescriptionDetailView(DetailView):
    template_name = "pages/model_description.html"
    context_object_name = "model"

    def get_queryset(self):
        return Model.objects.filter(pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stream"] = self.object.stream

        return context


model_description_detail_view = ModelDescriptionDetailView.as_view()


class DevelopmentActivityDetailView(DetailView):
    template_name = "pages/development_activity_detail.html"
    context_object_name = "activity"

    def get_queryset(self):
        return DevelopmentActivity.objects.filter(pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["layer"] = self.get_queryset().first().layer
        context["model"] = context["layer"].model

        return context


development_activity_detail_view = DevelopmentActivityDetailView.as_view()


class ProblemSolvingActivityDetailView(SingleTableView):
    template_name = "pages/problem_solving_activity_detail.html"
    context_object_name = "activity"
    table_class = MethodTableSimple

    def get_queryset(self):
        self.model = Model.objects.get(pk=self.kwargs["pk"])
        self.layer = self.model.layer.get(type=self.kwargs["layer"])
        self.development_activity = self.layer.development_activity.get(
            pk=self.kwargs["activity_pk"]
        )
        methods = None
        match self.kwargs["spalten"]:
            case "s":
                self.problem_solving_activity = self.development_activity.s
                methods = self.development_activity.method.filter(s_rating__gt=0)
            case "p":
                self.problem_solving_activity = self.development_activity.p
                methods = self.development_activity.method.filter(p_rating__gt=0)
            case "a":
                self.problem_solving_activity = self.development_activity.a
                methods = self.development_activity.method.filter(a_rating__gt=0)
            case "l":
                self.problem_solving_activity = self.development_activity.l
                methods = self.development_activity.method.filter(l_rating__gt=0)
            case "t":
                self.problem_solving_activity = self.development_activity.t
                methods = self.development_activity.method.filter(t_rating__gt=0)
            case "e":
                self.problem_solving_activity = self.development_activity.e
                methods = self.development_activity.method.filter(e_rating__gt=0)
            case "n":
                self.problem_solving_activity = self.development_activity.n
                methods = self.development_activity.method.filter(n_rating__gt=0)

        return methods

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["activity"] = self.problem_solving_activity
        context["layer"] = self.layer
        context["model"] = self.model
        context["development_activity"] = self.development_activity

        return context


problem_solving_activity_detail_view = ProblemSolvingActivityDetailView.as_view()
