# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.core.urlresolvers import (
    NoReverseMatch,
    reverse,
)

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
