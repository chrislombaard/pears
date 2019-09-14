# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys

from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile

from gallery.utils import load_image


class GalleryImage(models.Model):
    title = models.TextField()
    thumbnail = models.ImageField(upload_to="")
    width = models.IntegerField(default=600)
    height = models.IntegerField(default=600)

    def __str__(self):
        return self.title

    def save(self):
        img_obj = load_image(self.thumbnail)

        #change the imagefield value to be the newly modifed image value
        self.thumbnail = InMemoryUploadedFile(
            img_obj["img"], 'ImageField', self.thumbnail.name,
            img_obj["file_type"], sys.getsizeof(img_obj["img"]), None
        )
        self.width = img_obj["width"]
        self.height = img_obj["height"]
        super(GalleryImage, self).save()
