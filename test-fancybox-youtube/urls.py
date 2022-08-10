from django.urls import path

from . import views

urlpatterns = [
    # path(r'^$', views.Home.as_view(), name='home'),
    path('index', views.index, name='index')
]
