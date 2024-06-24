## 3.0.0 (2024-06-24)

* chore: convert HISTORY to markdown ([225cf17](https://github.com/bmihelac/django-cruds/commit/225cf17))


## 2.0.1 (unreleased)

-   Nothing changed yet.

## 2.0.0 (2022-04-26)

-   Django 3.2 compatibility, drop unmaintained Django versions

## 1.2.0 (2018-03-19)

-   feat: format_value RelatedManager support

## 1.1.0 (2018-03-14)

-   feat: add [crud_url]()\* shortcuts

## 1.0.0 (2018-03-14)

-   feat: Customizable CRUD url patterns with crud_urls
-   feat: crud_url fuction accepts model alongside with instances
-   feat: add crud_permission_name function
-   breaking: Django 1.11 and Django 2.0 compatibility Remove \< Django
    1.11 support
-   test coverage 100%

## 0.1.10 (2015-12-04)

-   Nothing changed yet.

## 0.1.9 (2015-12-04)

-   Nothing changed yet.

## 0.1.8 (2014-12-08)

-   `format_value` display FileField url

## 0.1.7 (2014-09-23)

-   Add optional prefix to crud_url_name, crud_url functions.

## 0.1.6 (2014-08-21)

-   ADD: cruds.util.crud_url function

## 0.1.5 (2014-07-01)

-   ADD: get_fields assignment_tag

## 0.1.4 (2014-06-30)

-   add human-readable name for the field's with choices

## 0.1.3 (2014-06-30)

-   append instead of prepending CRUD template name to a list of default
    candidate template names

## 0.1.2 (2014-06-10)

-   FIX: action url patterns should be in format /appname/model/3/edit/
    and not /appname/model/edit/3/
-   add `crud_fields` templatetag

## 0.1.1 (2014-06-09)

-   Handle and FK returns link to detail view if exists.
-   fixes and tweaks

## 0.1.0 (2014-06-08)

-   First release on PyPI.
