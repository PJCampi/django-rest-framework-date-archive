<div class="badges">
    <a href="http://travis-ci.org/PJCampi/django-rest-framework-date-archive">
        <img src="https://travis-ci.org/PJCampi/django-rest-framework-date-archive.svg?branch=master">
    </a>
    <a href="https://pypi.python.org/pypi/djangorestframework-date-archive">
        <img src="https://img.shields.io/pypi/v/djangorestframework-date-archive.svg">
    </a>
</div>

---

# djangorestframework-date-archive

Django date view archive for rest framework

---

## Overview

Django date view archive for rest framework

## Requirements

* Python (3.6)
* Django Rest Framework(3.8)

## Installation

Install using `pip`...

```bash
$ pip install djangorestframework-date-archive
```

## Example

rest_framework_date_archive provides your drf model viewsets with a read-only date archive similar to that of django.

The archive can be accessed through the following urls:
items\archive\year\
items\archive\year\month\
items\archive\year\month\day\

Setting things up is pretty easy:

Your model manager must include a queryset that inherit from DateArchiveMixin.
The name of the field with which the data is archived is specified by the class attribute date_field:

```python
class BlogQueryset(DateArchiveMixin,
                   models.QuerySet):
    date_field = 'date'


class Blog(models.Model):
    date = models.DateField()
    content = models.TextField(default='')

    objects = BlogQueryset.as_manager()
```

Your model viewset must inherit from DateArchiveView:

```python
class BlogViewSet(DateArchiveView,
                  ModelViewSet):
    model = Blog
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
```

And you must register your urls with the DateArchiveRouter:

```python
router = DateArchiveRouter()
router.register('blogs', BlogViewSet)
```


## Testing

Install testing requirements.

```bash
$ pip install -r requirements.txt
```

Run with tox.

You can also use the excellent [tox](http://tox.readthedocs.org/en/latest/) testing tool to run the tests against all supported versions of Python and Django. Install tox globally, and then simply run:

```bash
$ tox
```

## Documentation

To build the documentation, you'll need to install `mkdocs`.

```bash
$ pip install mkdocs
```

To preview the documentation:

```bash
$ mkdocs serve
Running at: http://127.0.0.1:8000/
```

To build the documentation:

```bash
$ mkdocs build
```
