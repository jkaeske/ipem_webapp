import django_tables2 as tables

from .models import Method


class MethodTable(tables.Table):
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
    alternative_name = tables.Column(
        verbose_name="Alternative Names",
        accessor="alternative_name",
        attrs={
            "th": {
                "class": ("px-3 py-3.5 text-left text-sm font-semibold text-gray-900")
            },
            "td": {"class": "whitespace-nowrap px-3 py-4 text-sm text-gray-500"},
        },
    )
    view = tables.LinkColumn(
        "methods:method_detail",
        orderable=False,
        args=[tables.A("pk"), "abstract"],
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
        model = Method
        fields = ("name", "alternative_name", "view")
        attrs = {
            "class": "min-w-full divide-y divide-gray-300",
            "tbody": {"class": "divide-y divide-gray-200 bg-white"},
        }
        paginator_class = (
            tables.LazyPaginator
        )  # Use the LazyPaginator for better performance
        paginate_by = 25  # Set the number of rows per page
        template_name = "tailwind_table.html"
