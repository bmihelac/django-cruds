from django.test.testcases import TestCase

import django
from django.views import View

from cruds import views
from cruds.urls import (
    crud_urls,
    crud_for_model,
    crud_for_app,
)

from tests.testapp.models import (
    Author,
)


def get_url_regex(url):
    if django.VERSION < (2, 0):
        return url.regex.pattern
    return url.pattern.regex.pattern


class TestUrls(TestCase):

    def setUp(self):
        super(TestUrls, self).setUp()
        self.view = View.as_view()

    def test_crud_urls(self):
        urls = crud_urls(
            Author,
            list_view=self.view,
        )
        self.assertEqual(len(urls), 1)
        url = urls[0]
        self.assertEqual(url.name, 'testapp_author_list')
        self.assertSequenceEqual(get_url_regex(url), r'^$')

    def test_crud_urls_kwargs(self):
        urls = crud_urls(
            Author,
            additional=self.view,
        )
        self.assertEqual(len(urls), 1)
        url = urls[0]
        self.assertEqual(url.name, 'testapp_author_additional')
        self.assertSequenceEqual(
            get_url_regex(url),
            r'^(?P<pk>\d+)/additional/$'
        )

    def test_crud_urls_url_prefix(self):
        urls = crud_urls(
            Author,
            list_view=self.view,
            url_prefix=r'^author/'
        )
        self.assertEqual(get_url_regex(urls[0]), '^author/$')

    def test_crud_urls_name_prefix(self):
        urls = crud_urls(
            Author,
            list_view=self.view,
            name_prefix='my_'
        )
        self.assertEqual(urls[0].name, 'my_testapp_author_list')

    def test_crud_urls_list_views(self):
        urls = crud_urls(
            Author,
            list_views={
                'aggregate': self.view,
                'aggregate2': self.view,
            }
        )
        url_names = [url.name for url in urls]
        self.assertTrue('testapp_author_aggregate' in url_names)
        self.assertTrue('testapp_author_aggregate2' in url_names)

    def test_crud_for_model(self):
        urls = crud_for_model(Author)
        self.assertEqual(len(urls), 5)
        self.assertEqual(urls[0].name, 'testapp_author_list')
        self.assertIs(urls[0].callback.view_class, views.CRUDListView)
        self.assertEqual(urls[1].name, 'testapp_author_create')
        self.assertIs(urls[1].callback.view_class, views.CRUDCreateView)
        self.assertEqual(urls[2].name, 'testapp_author_detail')
        self.assertIs(urls[2].callback.view_class, views.CRUDDetailView)
        self.assertEqual(urls[3].name, 'testapp_author_update')
        self.assertIs(urls[3].callback.view_class, views.CRUDUpdateView)
        self.assertEqual(urls[4].name, 'testapp_author_delete')
        self.assertIs(urls[4].callback.view_class, views.CRUDDeleteView)

    def test_cruds_for_app(self):
        urls = crud_for_app('testapp')
        self.assertNotEqual(len(urls), 0)
