from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from os import sys
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mainapp.urls")),
]

ENABLE_DEBUG_TOOLBAR = settings.DEBUG and "test" not in sys.argv
if ENABLE_DEBUG_TOOLBAR:
    urlpatterns = urlpatterns  + debug_toolbar_urls()
