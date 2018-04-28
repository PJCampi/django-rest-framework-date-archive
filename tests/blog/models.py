from django.db import models

from rest_framework_date_archive import DateArchiveMixin


class BlogQueryset(DateArchiveMixin,
                   models.QuerySet):
    archive_field = 'date'


class Blog(models.Model):
    date = models.DateField()
    content = models.TextField(default='')

    objects = BlogQueryset.as_manager()


class BlogTime(models.Model):
    date = models.DateTimeField()
    content = models.TextField(default='')

    objects = BlogQueryset.as_manager()

