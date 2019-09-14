# Generated by Django 2.2 on 2019-09-07 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('width', models.IntegerField(default=600)),
                ('height', models.IntegerField(default=600)),
            ],
        ),
    ]