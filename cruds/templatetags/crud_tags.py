# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Model
from django import template
from django.core.urlresolvers import (
    NoReverseMatch,
    reverse,
)
from django.utils.html import escape
from django.utils.safestring import mark_safe

from cruds import utils


register = template.Library()


@register.filter
def get_attr(obj, attr):
    """
    Filter returns obj attribute.
    """
    return getattr(obj, attr)


@register.assignment_tag
def crud_url(obj, action):
    try:
        url = reverse(
            utils.crud_url_name(type(obj), action),
            kwargs={'pk': obj.pk})
    except NoReverseMatch:
        url = None
    return url


@register.filter
def format_value(obj, field_name):
    """
    Simple value formatting.

    If value is model instance returns link to detail view if exists.
    """
    value = getattr(obj, field_name)
    if isinstance(value, Model):
        url = crud_url(value, utils.ACTION_DETAIL)
        if url:
            return mark_safe('<a href="%s">%s</a>' % (url, escape(value)))
    return value
