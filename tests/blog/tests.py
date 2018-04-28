from datetime import date

from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

from unittest.mock import patch

from .models import Blog, DateArchiveMixin


class TestQuerySetDate(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()

    @classmethod
    def setUpTestData(cls):
        Blog.objects.create(date=date(2017, 1, 1))
        Blog.objects.create(date=date(2018, 1, 1))
        Blog.objects.create(date=date(2018, 2, 1))
        Blog.objects.create(date=date(2018, 2, 2))
        Blog.objects.create(date=date(2018, 2, 3))

    @patch('rest_framework_date_archive.querysets.timezone_today')
    def test_queryset(self, today_func):
        today_func.return_value = date(2018, 2, 2)

        # allow future is False
        self.assertEqual(5, Blog.objects.count())
        self.assertEqual(3, Blog.objects.get_period(2018).count())
        self.assertEqual(2, Blog.objects.get_period(2018, 2).count())
        self.assertEqual(1, Blog.objects.get_period(2018, 2, 2).count())
        self.assertEqual(0, Blog.objects.get_period(2018, 2, 3).count())

        # test earliest and latest
        self.assertEqual(1, Blog.objects.get_earliest_period('year').count())
        self.assertEqual(3, Blog.objects.get_latest_period('year').count())
        self.assertEqual(2, Blog.objects.get_latest_period('month').count())
        self.assertEqual(1, Blog.objects.get_latest_period('day').count())

        # what if we allow future
        DateArchiveMixin.allow_future = True
        self.assertEqual(1, Blog.objects.get_period(2018, 2, 3).count())
        self.assertEqual(3, Blog.objects.get_period(2018, 2).count())
        self.assertEqual(3, Blog.objects.get_latest_period('month').count())

        # incorrect input
        with self.assertRaises(Exception):
            Blog.objects.get_period(2018, None, 1)


    @patch('rest_framework_date_archive.querysets.timezone_today')
    def test_get_urls(self, today_func):
        today_func.return_value = date(2018, 2, 2)

        self.assertEqual(5, len(self.client.get(reverse('blog-list')).data))

        url = reverse('blog-archive-year', kwargs={'year': 2018})
        self.assertEqual('/tests/blogs/archive/2018/', url)
        self.assertEqual(3, len(self.client.get(url).data))

        url = reverse('blog-archive-month', kwargs={'year': 2018, 'month': 2})
        self.assertEqual('/tests/blogs/archive/2018/2/', url)
        self.assertEqual(2, len(self.client.get(url).data))

        url = reverse('blog-archive-day', kwargs={'year': 2018, 'month': 2, 'day': 2})
        self.assertEqual('/tests/blogs/archive/2018/2/2/', url)
        self.assertEqual(1, len(self.client.get(url).data))
