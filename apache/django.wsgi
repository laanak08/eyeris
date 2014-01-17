#!/usr/bin/python
import os, sys
sys.path.append('/cpm/projects/')
sys.path.append('/cpm/projects/smapi_browser')
os.environ['DJANGO_SETTINGS_MODULE'] = 'smapi.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
