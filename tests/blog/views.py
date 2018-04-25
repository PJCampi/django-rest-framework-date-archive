from rest_framework.viewsets import ModelViewSet
from rest_framework_date_archive import DateArchiveView

from .models import Blog, BlogTime
from .serializers import BlogSerializer, BlogTimeSerializer


class BlogViewSet(DateArchiveView,
                  ModelViewSet):
    model = Blog
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogTimeViewSet(DateArchiveView,
                      ModelViewSet):
    model = BlogTime
    queryset = BlogTime.objects.all()
    serializer_class = BlogTimeSerializer
