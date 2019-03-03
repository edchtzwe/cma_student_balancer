from django.conf.urls import url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf.urls import include
from django.urls import path
# remove this on prod
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    path('balancer/', include('balancer.urls')),
    path('', RedirectView.as_view(url='/balancer/')),
    # static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]