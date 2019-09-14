from rest_framework import serializers
from gallery.models import GalleryImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ("thumbnail", "title")
        read_only_fields = ("thumbnail",)
