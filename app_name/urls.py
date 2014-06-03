# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, unicode_literals)

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('{{ app_name }}.views',
    # Define your urls here
)

# Automatic namespaced URLs
named_patterns = (urlpatterns, '{{ app_name }}', '{{ app_name }}')
