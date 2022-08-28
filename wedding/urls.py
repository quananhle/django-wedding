from django.urls import path

from . import views

urlpatterns = [
    # path(r'^$', views.Home.as_view(), name='home'),
    # path('home', views.Home.as_view(), name='home'),
    path('', views.Home.as_view(), name='home'),
    path('home/hanoi', views.hanoi, name='hanoi'),
    path('home/engagement', views.engagement, name='engagement'),
    path('home/wedding', views.wedding, name='wedding-party')
]
