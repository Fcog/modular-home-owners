"""mhoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail_multi_image_edit.views import multi_image_edit
from wagtail_multi_upload.views import add as add_multiple_fix
from wagtail.contrib.sitemaps.views import sitemap
from machina import urls as machina_urls


from .settings import DEVELOPMENT_MODE, DEBUG_BAR
from mhoapp.base import views

if DEVELOPMENT_MODE is True & DEBUG_BAR is True:
    import debug_toolbar

urlpatterns = [
    path('admin/images/multi-edit/', multi_image_edit, name='multi_image_edit'),
    path('multi-add-fix/', add_multiple_fix, name='add_multiple_fix'),
    path('admin/forum', admin.site.urls),
    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('', include('mhoapp.authentication.urls')),
    path('upload_image/', views.upload_image),
    path('tinymce/', include('tinymce.urls')),
    path('forum/', include(machina_urls), name='forum'),
     path('sitemap.xml', sitemap),
]

# Include UI pattern library URL before the Wagtail URLs.
if DEVELOPMENT_MODE is True:
    urlpatterns += [
        path('pattern-library/', include('pattern_library.urls')),
    ]

if DEVELOPMENT_MODE is True & DEBUG_BAR is True:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

# Include Wagtail URLs last.
urlpatterns += [
    path(r'', include(wagtail_urls)),
]

if DEVELOPMENT_MODE is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
