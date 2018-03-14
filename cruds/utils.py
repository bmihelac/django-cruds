# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.db.models import Model

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

MAP_PERMISSION_ACTIONS = {
    'create': 'add',
    'update': 'change',
}


def crud_url_name(model, action, prefix=None):
    """
    Returns url name for given model and action.
    """
    if prefix is None:
        prefix = ""
    app_label = model._meta.app_label
    model_lower = model.__name__.lower()
    return '%s%s_%s_%s' % (prefix, app_label, model_lower, action)


def get_fields(model, include=None):
    """
    Returns ordered dict in format 'field': 'verbose_name'
    """
    fields = OrderedDict()
    info = model._meta
    if include:
        selected = [info.get_field(name) for name in include]
    else:
        selected = [field for field in info.fields if field.editable]
    for field in selected:
        fields[field.name] = field.verbose_name
    return fields


def crud_url(instance_or_model, action, prefix=None, additional_kwargs=None):
    """Shortcut function returns URL for instance or model and action.

    Example::

        crud_url(author, 'update')

    Is same as:

        reverse('testapp_author_update', kwargs={'pk': author.pk})

    Example::

        crud_url(Author, 'update')

    Is same as:

        reverse('testapp_author_list')
    """
    if additional_kwargs is None:
        additional_kwargs = {}
    if isinstance(instance_or_model, Model):
        additional_kwargs['pk'] = instance_or_model.pk
        model_name = instance_or_model._meta.model
    else:
        model_name = instance_or_model
    return reverse(
        crud_url_name(model_name, action, prefix),
        kwargs=additional_kwargs
    )


def crud_url_list(model, *args, **kwargs):
    return crud_url(model, ACTION_LIST, *args, **kwargs)


def crud_url_detail(instance, *args, **kwargs):
    return crud_url(instance, ACTION_DETAIL, *args, **kwargs)


def crud_url_update(instance, *args, **kwargs):
    return crud_url(instance, ACTION_UPDATE, *args, **kwargs)


def crud_url_create(model, *args, **kwargs):
    return crud_url(model, ACTION_CREATE, *args, **kwargs)


def crud_url_delete(instance, *args, **kwargs):
    return crud_url(instance, ACTION_DELETE, *args, **kwargs)


def crud_permission_name(model, action, convert=True):
    """Returns permission name using Django naming convention: app_label.action_object.

    If `convert` is True, `create` and `update` actions would be renamed
    to `add` and `change`.
    """
    app_label = model._meta.app_label
    model_lower = model.__name__.lower()
    if convert:
        action = MAP_PERMISSION_ACTIONS.get(action, action)
    return '%s.%s_%s' % (
        app_label,
        action,
        model_lower
    )
