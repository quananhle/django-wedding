from django.urls import path

from . import views

urlpatterns = [
    # path(r'^$', views.Home.as_view(), name='home'),
    # path('home', views.Home.as_view(), name='home'),
    path('', views.Home.as_view(), name='home'),
    path('home/hanoi', views.hanoi, name='hanoi'),
    path('home/cantho', views.cantho, name='cantho'),
    path('home/engagement', views.engagement, name='engagement'),
    path('home/wedding', views.wedding, name='wedding-party'),
    path('home/save-the-dates', views.save_the_date, name='save-the-dates-photos')
]
