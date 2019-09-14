from django.forms import ModelForm
from gallery.models import GalleryImage


class UploadImageForm(ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['title', 'thumbnail']