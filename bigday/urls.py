from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    # path(r'^', include('wedding.urls')),
    path('', include('wedding.urls')),
    path(r'^', include('guests.urls')),
    path(r'^admin/', admin.site.urls),
    # path('^accounts/', include('django.contrib.auth.urls'))
]
