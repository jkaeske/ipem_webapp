import nested_admin
from django.contrib import admin

from .models import DevelopmentActivity, Layer, Model


class DevelopmentActivityInline(nested_admin.NestedTabularInline):
    model = DevelopmentActivity
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
