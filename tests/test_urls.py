from django.test.testcases import TestCase

from django.views import View

from cruds import views
from cruds.urls import (
    crud_urls,
    crud_for_model,
)

from tests.testapp.models import (
    Author,
)


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
        self.assertSequenceEqual(url.regex.pattern, r'^$')

    def test_crud_urls_url_prefix(self):
        urls = crud_urls(
            Author,
            list_view=self.view,
            url_prefix=r'^author/'
        )
        self.assertEqual(urls[0].regex.pattern, '^author/$')

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
        self.assertEqual(urls[0].name, 'testapp_author_aggregate')
        self.assertEqual(urls[1].name, 'testapp_author_aggregate2')

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
