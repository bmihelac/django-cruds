# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
