from django.test.testcases import TestCase

from cruds import utils

from tests.testapp.models import (
    Author,
)


class TestUtils(TestCase):

    def test_get_fields_order(self):
        res = utils.get_fields(Author, ('birthday', 'name'))
        self.assertEqual(list(res.keys())[0], 'birthday')

    def test_crud_permission_name(self):
        self.assertEqual(
            utils.crud_permission_name(Author, utils.ACTION_UPDATE),
            'testapp.change_author'
        )
        self.assertEqual(
            utils.crud_permission_name(Author, utils.ACTION_CREATE),
            'testapp.add_author'
        )
        self.assertEqual(
            utils.crud_permission_name(Author, utils.ACTION_LIST),
            'testapp.list_author'
        )

    def test_crud_url_for_instance(self):
        instance = Author.objects.create(name='foo')
        self.assertEqual(
            utils.crud_url(instance, utils.ACTION_DETAIL),
            '/testapp/author/1/'
        )

    def test_crud_url_for_model(self):
        self.assertEqual(
            utils.crud_url(Author, utils.ACTION_LIST),
            '/testapp/author/'
        )

    def test_crud_url_shortcuts(self):
        instance = Author.objects.create(name='foo')

        self.assertEqual(
            utils.crud_url_list(Author),
            '/testapp/author/'
        )
        self.assertEqual(
            utils.crud_url_create(Author),
            '/testapp/author/new/'
        )
        self.assertEqual(
            utils.crud_url_detail(instance),
            '/testapp/author/1/'
        )
        self.assertEqual(
            utils.crud_url_update(instance),
            '/testapp/author/1/edit/'
        )
        self.assertEqual(
            utils.crud_url_delete(instance),
            '/testapp/author/1/remove/'
        )
