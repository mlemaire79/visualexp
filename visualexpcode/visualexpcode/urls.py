"""visualexpcode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from visualAdmin.views.views import ArtworkList
from visualAdmin.views.admin.display import ExpoListView
from visualexpcode.views import Admin
from visualexpcode.views import ArtworkTest
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/manage/displays/$', ExpoListView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^artwork/$', ArtworkList.as_view()),
    url(r'^$', admin.site.urls),
    url(r'^bootstrap/$', ArtworkTest.as_view()),
    url(r'^admin_tools/', include('admin_tools.urls')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
