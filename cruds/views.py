# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import OrderedDict

from django.core.urlresolvers import (
    NoReverseMatch,
    reverse,
)
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import utils


class CRUDMixin(object):

    def get_context_data(self, **kwargs):
        """
        Adds available urls and names.
        """
        context = super(CRUDMixin, self).get_context_data(**kwargs)
        context.update({
            'model_verbose_name': self.model._meta.verbose_name,
            'model_verbose_name_plural': self.model._meta.verbose_name_plural,
        })

        fields = OrderedDict()
        for field in self.model._meta.fields:
            if field.editable:
                fields[field.name] = field.verbose_name
        context['fields'] = fields

        if hasattr(self, 'object') and self.object:
            for action in utils.INSTANCE_ACTIONS:
                try:
                    url = reverse(
                        utils.crud_url_name(self.model, action),
                        kwargs={'pk': self.object.pk})
                except NoReverseMatch:
                    url = None
                context['url_%s' % action] = url

        for action in utils.LIST_ACTIONS:
            try:
                url = reverse(utils.crud_url_name(self.model, action))
            except NoReverseMatch:
                url = None
            context['url_%s' % action] = url

        return context

    def get_success_url(self):
        return reverse(
            utils.crud_url_name(self.model, utils.ACTION_DETAIL),
            kwargs={'pk': self.object.pk})


class CRUDCreateView(CRUDMixin, CreateView):
    template_name = 'cruds/create.html'


class CRUDDeleteView(CRUDMixin, DeleteView):
    template_name = 'cruds/delete.html'

    def get_success_url(self):
        return reverse(utils.crud_url_name(self.model, utils.ACTION_LIST))


class CRUDDetailView(CRUDMixin, DetailView):
    template_name = 'cruds/detail.html'


class CRUDListView(CRUDMixin, ListView):
    template_name = 'cruds/list.html'


class CRUDUpdateView(CRUDMixin, UpdateView):
    template_name = 'cruds/update.html'
