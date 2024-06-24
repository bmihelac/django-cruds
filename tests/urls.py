# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include
from django.contrib import admin

from cruds.urls import crud_for_app
from django.urls import path


urlpatterns = [
    path('admin/', include(admin.site.urls)),
]


# add crud for whole app
urlpatterns += crud_for_app('testapp')

# add crud for one model

# from django.db.models.loading import get_model
# from cruds.urls import crud_for_model
# urlpatterns += crud_for_model(get_model('testapp', 'Author'))
