import nested_admin
from django.contrib import admin

from ipem_webapp.methods.models import MethodRegistry

from .models import DevelopmentActivity, Layer, Model, ProblemSolvingActivity


class DevelopmentActivityInline(nested_admin.NestedTabularInline):
    model = DevelopmentActivity
    fields = [
        "name",
        "order",
        "parent",
        "s",
        "p",
        "a",
        "l",
        "t",
        "e",
        "n",
    ]
    readonly_fields = [
        "s",
        "p",
        "a",
        "l",
        "t",
        "e",
        "n",
    ]
    extra = 0


class LayerInline(nested_admin.NestedStackedInline):
    model = Layer
    extra = 0
    inlines = [DevelopmentActivityInline]


class ModelAdmin(nested_admin.NestedModelAdmin):
    readonly_fields = ("pk",)
    search_fields = [
        "name",
    ]
    list_display = ["pk", "name"]
    inlines = [
        LayerInline,
    ]


admin.site.register(Model, ModelAdmin)

admin.site.register(ProblemSolvingActivity)


class MethodRegistryInline(admin.TabularInline):
    model = MethodRegistry
    extra = 0


class DevelopmentActivityAdmin(admin.ModelAdmin):
    readonly_fields = [
        "s",
        "p",
        "a",
        "l",
        "t",
        "e",
        "n",
    ]
    list_display = [
        "name",
        "get_layer",
        "get_model",
    ]
    inlines = [
        MethodRegistryInline,
    ]

    @admin.display(ordering="layer", description="Layer")
    def get_layer(self, obj):
        return obj.layer.type

    @admin.display(ordering="layer__model", description="Model")
    def get_model(self, obj):
        return obj.layer.model


admin.site.register(DevelopmentActivity, DevelopmentActivityAdmin)
