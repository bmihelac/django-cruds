# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.core.urlresolvers import reverse
from django.db.models import get_app, get_models
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import utils
from .views import CRUDMixin


def crud_for_model(dest_model, urlprefix=None):
    """
    Returns list of ``url`` items to CRUD a model.
    """
    model_lower = dest_model.__name__.lower()

    if urlprefix is None:
        urlprefix = ''
    urlprefix += model_lower

    urls = []

    class CRUDCreateView(CRUDMixin, CreateView):
        model = dest_model
        fields = [f.name for f in dest_model._meta.fields]
        crud_template_name = 'cruds/create.html'

    class CRUDDeleteView(CRUDMixin, DeleteView):
        model = dest_model
        crud_template_name = 'cruds/delete.html'

        def get_success_url(self):
            return reverse(utils.crud_url_name(self.model, utils.ACTION_LIST))

    class CRUDDetailView(CRUDMixin, DetailView):
        model = dest_model
        fields = [f.name for f in dest_model._meta.fields]
        crud_template_name = 'cruds/detail.html'

    class CRUDListView(CRUDMixin, ListView):
        model = dest_model
        fields = [f.name for f in dest_model._meta.fields]
        crud_template_name = 'cruds/list.html'

    class CRUDUpdateView(CRUDMixin, UpdateView):
        model = dest_model
        fields = [f.name for f in dest_model._meta.fields]
        crud_template_name = 'cruds/update.html'

    urls.append(url(
        r'%s/new/$' % urlprefix,
        CRUDCreateView.as_view(),
        name=utils.crud_url_name(dest_model, utils.ACTION_CREATE)
    ))

    urls.append(url(
        r'%s/(?P<pk>\d+)/remove/$' % urlprefix,
        CRUDDeleteView.as_view(model=dest_model),
        name=utils.crud_url_name(dest_model, utils.ACTION_DELETE)
    ))

    urls.append(url(
        r'%s/(?P<pk>\d+)/$' % urlprefix,
        CRUDDetailView.as_view(model=dest_model),
        name=utils.crud_url_name(dest_model, utils.ACTION_DETAIL)
    ))

    urls.append(url(
        r'%s/(?P<pk>\d+)/edit/$' % urlprefix,
        CRUDUpdateView.as_view(model=dest_model),
        name=utils.crud_url_name(dest_model, utils.ACTION_UPDATE)
    ))

    urls.append(url(
        r'%s/$' % urlprefix,
        CRUDListView.as_view(model=dest_model),
        name=utils.crud_url_name(dest_model, utils.ACTION_LIST)
    ))

    return urls


def crud_for_app(app_label, urlprefix=None):
    """
    Returns list of ``url`` items to CRUD an app.
    """
    if urlprefix is None:
        urlprefix = app_label + '/'
    app = get_app(app_label)
    urls = []
    for model in get_models(app):
        urls += crud_for_model(model, urlprefix)
    return urls
