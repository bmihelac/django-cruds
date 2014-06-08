# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template


register = template.Library()


@register.filter
def get_attr(obj, attr):
    """
    Filter returns obj attribute.
    """
    return getattr(obj, attr)
