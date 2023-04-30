import django_tables2 as tables

from .models import Model


class ModelTable(tables.Table):
    name = tables.Column(
        verbose_name="Name",
        accessor="name",
        attrs={
            "th": {
                "class": (
                    "py-3.5 pl-6 pr-3 text-left text-sm font-semibold "
                    "text-gray-900 sm:pl-0"
                ),
            },
            "td": {
                "class": (
                    "whitespace-nowrap py-4 pl-6 pr-3 text-sm font-medium "
                    "text-gray-900 sm:pl-0"
                )
            },
        },
    )
    view = tables.LinkColumn(
        "models:model_detail",
        orderable=False,
        args=[tables.A("pk"), "PRODUCT"],
        text="View",
        verbose_name="",
        attrs={
            "a": {"class": "text-emerald-600 hover:text-emerald-900"},
            "th": {
                "class": "px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
            },
            "td": {
                "class": (
                    "whitespace-nowrap py-4 pl-3 pr-6 text-right text-sm "
                    "font-medium sm:pr-0"
                )
            },
        },
    )

    class Meta:
        model = Model
        fields = ("name", "view")
        attrs = {
            "class": "min-w-full divide-y divide-gray-300",
            "tbody": {"class": "divide-y divide-gray-200 bg-white"},
        }
        paginator_class = (
            tables.LazyPaginator
        )  # Use the LazyPaginator for better performance
        paginate_by = 25  # Set the number of rows per page
        template_name = "tailwind_table.html"
