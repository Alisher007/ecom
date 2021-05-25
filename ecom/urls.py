from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('accounts/', include('accounts.urls') ),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'ecom admin'
admin.site.site_title = 'ecom admin'
admin.site.site_url = 'http://ecom.com/'
admin.site.index_title = 'ecom administration'