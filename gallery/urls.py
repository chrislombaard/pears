from django.urls import path

from gallery.views import GalleryView, UploadImageView, ImageUploadView

app_name = "gallery"

urlpatterns = [
    path("", GalleryView.as_view(), name="index"),
    path("upload/", UploadImageView.as_view(), name="upload"),
    path("upload_drf/<title>/", ImageUploadView.as_view(), name="upload_drf"),
]
