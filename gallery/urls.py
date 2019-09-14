from django.urls import path

from gallery.views import GalleryView, UploadImageView

app_name = "gallery"

urlpatterns = [
    path("", GalleryView.as_view(), name="index"),
    path("upload/", UploadImageView.as_view(), name="upload"),
]
