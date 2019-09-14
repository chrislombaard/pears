# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from gallery.models import GalleryImage
from gallery.forms import UploadImageForm
from gallery.serializers import ImageSerializer


class GalleryView(ListView):
    model = GalleryImage
    template_name = "gallery/index.html"


class UploadImageView(CreateView):
    model = GalleryImage
    form_class = UploadImageForm
    template_name = "gallery/upload.html"
    success_url = reverse_lazy("gallery:index")
