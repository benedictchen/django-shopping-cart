from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'ecommerce.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', 'products.views.home', name='home'),
                       url(r'^products/(?P<slug>[^\/]+)\/add$', 'carts.views.add_to_cart', name='add_to_cart'),
                       url(r'^products/(?P<id>\d+)\/remove$', 'carts.views.remove_from_cart',
                           name='remove_from_cart'),
                       url(r'^products/(?P<slug>[^\/]+)\/?', 'products.views.detail', name='detail'),
                       url(r'^products/', 'products.views.all', name='all'),
                       url(r'^search/', 'products.views.search', name='search'),
                       url(r'^cart/', 'carts.views.view_cart', name='view_cart'),
                       url(r'^checkout/', 'orders.views.checkout', name='checkout'),
                       url(r'^orders/', 'orders.views.orders', name='orders'),
                       url(r'^admin/', include(admin.site.urls)),
)

# Serve static assets in dev
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
