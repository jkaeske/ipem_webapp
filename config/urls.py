from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    path(
        "meta_model/",
        TemplateView.as_view(template_name="pages/meta_model.html"),
        name="meta_model",
    ),
    path(
        "method_abstract/",
        TemplateView.as_view(template_name="pages/method_abstract.html"),
        name="method_abstract",
    ),
    path(
        "meta_model/spalten/",
        TemplateView.as_view(template_name="spalten.html"),
        name="spalten",
    ),
    path(
        "meta_model/manage_projects/",
        TemplateView.as_view(template_name="manage_projects.html"),
        name="manage_projects",
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    path("_nested_admin/", include("nested_admin.urls")),
    # Streamfield blocks
    path("streamfield/", include("streamfield.urls")),
    # User management
    path("users/", include("ipem_webapp.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path("methods/", include("ipem_webapp.methods.urls")),
    path("models/", include("ipem_webapp.models.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
