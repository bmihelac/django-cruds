# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import OrderedDict


ACTION_CREATE = 'create'
ACTION_DELETE = 'delete'
ACTION_DETAIL = 'detail'
ACTION_LIST = 'list'
ACTION_UPDATE = 'update'

INSTANCE_ACTIONS = (
    ACTION_DELETE,
    ACTION_DETAIL,
    ACTION_UPDATE,
)
LIST_ACTIONS = (
    ACTION_CREATE,
    ACTION_LIST,
)

ALL_ACTIONS = LIST_ACTIONS + INSTANCE_ACTIONS


def crud_url_name(model, action):
    """
    Returns url name for given model and action.
    """
    app_label = model._meta.app_label
    model_lower = model.__name__.lower()
    return '%s_%s_%s' % (app_label, model_lower, action)


def get_fields(model, include=None):
    """
    Returns ordered dict in format 'field': 'verbose_name'
    """
    fields = OrderedDict()
    for field in model._meta.fields:
        if include is not None and field.name not in include:
            continue
        if field.editable:
            fields[field.name] = field.verbose_name
    return fields
