from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'books.views.home'),
    url(r'^book/(?P<alias>[^/]+)', 'books.views.item'),
    url(r'^recently/', 'books.views.recently'),
    url(r'^author/(?P<alias>[^/]+)', 'books.views.author'),
    url(r'^categories/fiction/', 'books.views.categories_fiction'),
    url(r'^categories/science/', 'books.views.categories_science'),
    url(r'^categories/detective/', 'books.views.categories_detective'),
    url(r'^categories/technical/', 'books.views.categories_technical'),
    url(r'^search/', 'books.views.search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)