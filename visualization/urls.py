from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Dataset endpoints
    path("datasets/", views.DatasetListCreateView.as_view(), name="dataset-list-create"),
    path("datasets/<int:pk>/", views.DatasetDetailView.as_view(), name="dataset-detail"),

    # Entity endpoints
    path("entities/", views.EntityListCreateView.as_view(), name="entity-list-create"),
    path("entities/<int:pk>/", views.EntityDetailView.as_view(), name="entity-detail"),

    # Detail endpoints
    path("details/", views.DetailListCreateView.as_view(), name="detail-list-create"),
    path("details/<int:pk>/", views.DetailDetailView.as_view(), name="detail-detail"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
