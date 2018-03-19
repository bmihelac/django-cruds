# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Continent(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Continent'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/'


@python_2_unicode_compatible
class Country(models.Model):
    name = models.CharField(max_length=100)
    continent = models.ForeignKey(
        Continent,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateTimeField(auto_now_add=True)
    document = models.FileField(
        upload_to='testapp/',
        verbose_name='document',
        blank=True
    )
    user = models.ForeignKey(
        User,
        verbose_name='user',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def get_birthday_display(self):
        return '!' + str(self.birthday) + '!'
