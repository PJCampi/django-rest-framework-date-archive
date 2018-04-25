from rest_framework.serializers import ModelSerializer

from .models import Blog, BlogTime


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        exclude = ()


class BlogTimeSerializer(ModelSerializer):
    class Meta:
        model = BlogTime
        exclude = ()
