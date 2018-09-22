from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from pms import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^setup/', include('setup.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^feedback/$', views.feedback, name='feedback'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
