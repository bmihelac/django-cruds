# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import re_path
from django.contrib import admin

from cruds.urls import (
    crud_for_model,
)
from .models import Author, Country


urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
]


# add crud for whole app
urlpatterns += crud_for_model(Author, urlprefix="testapp/")
urlpatterns += crud_for_model(Country, urlprefix="testapp/")
