from datetime import date
from collections import namedtuple

from django.test.testcases import TestCase
from django.template import Context, Template

from tests.testapp.models import (
    Author,
    Country,
    Continent,
)


class TestTags(TestCase):

    def setUp(self):
        self.author = Author.objects.create(name='Foo')

    def test_get_attr(self):
        template = Template(
            '''
            {% load crud_tags %}
            {{ obj|get_attr:"attr" }}
            ''')

        SomeType = namedtuple('SomeType', ['attr'])
        context = Context({'obj': SomeType(attr='foo')})
        res = template.render(context)
        self.assertIn('foo', res.strip())

    def test_crud_url(self):
        context = Context({'instance': self.author})
        template = Template(
            '{% load crud_tags %}{% crud_url instance "detail" %}')
        res = template.render(context)
        self.assertEqual(res, '/testapp/author/1/')

        template = Template(
            '{% load crud_tags %}{% crud_url instance "nonexisting" %}')
        res = template.render(context)
        self.assertEqual(res, 'None')

    def test_format_value(self):
        context = Context({'instance': self.author})

        self.author.birthday = date(2000, 1, 1)
        template = Template(
            '{% load crud_tags %}{{ instance|format_value:"name" }}')
        res = template.render(context)
        self.assertEqual(res, 'Foo')

        template = Template(
            '{% load crud_tags %}{{ instance|format_value:"birthday" }}')
        res = template.render(context)
        self.assertEqual(res, '!2000-01-01!')

        self.author.document = '/document.pdf'
        template = Template(
            '{% load crud_tags %}{{ instance|format_value:"document" }}')
        res = template.render(context)
        self.assertEqual(res, '<a href="/document.pdf">document.pdf</a>')

        self.author.country = Country.objects.create(name='Fooland')
        template = Template(
            '{% load crud_tags %}{{ instance|format_value:"country" }}')
        res = template.render(context)
        self.assertEqual(res, '<a href="/testapp/country/1/">Fooland</a>')

        self.author.country.continent = Continent.objects.create(
            name='Foontinent')
        template = Template(
            '{% load crud_tags %}{{ instance.country|format_value:"continent" }}')
        res = template.render(context)
        self.assertEqual(res, '<a href="/">Foontinent</a>')

        delattr(Continent, 'get_absolute_url')
        template = Template(
            '{% load crud_tags %}{{ instance.country|format_value:"continent" }}')
        res = template.render(context)
        self.assertEqual(res, 'Foontinent')

    def test_format_value_queryset(self):
        continent = Continent.objects.create(name='Foontinent')
        continent.country_set.create(name='Fooland')
        continent.country_set.create(name='Barland')
        template = Template(
            '{% load crud_tags %}{{ instance|format_value:"country_set" }}')
        res = template.render(Context({'instance': continent}))
        self.assertEqual(
            res,
            '<a href="/testapp/country/1/">Fooland</a>, <a href="/testapp/country/2/">Barland</a>'  # noqa
        )

    def test_crud_fields(self):
        context = Context({'instance': self.author})

        template = Template(
            '{% load crud_tags %}{% crud_fields instance %}')
        res = template.render(context)

        template = Template(
            '{% load crud_tags %}{% crud_fields instance "name" %}')
        res = template.render(context)
        self.assertIn('Foo', res)

    def test_get_fields(self):
        context = Context({'instance': self.author})
        template = Template(
            '{% load crud_tags %}{% get_fields instance %}')
        res = template.render(context)
