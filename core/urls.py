from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from wkhtmltopdf.views import PDFTemplateView

urlpatterns = [
    path('warehouse/', include('warehouse.urls')),
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls')),
    path('stock/', include('stockmgmt.urls')),
    url(r'^download/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}),
    url(r'^pdf/$', PDFTemplateView.as_view(template_name='invoice/invoice.html',
                                           filename='invoice.pdf'), name='pdf'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

