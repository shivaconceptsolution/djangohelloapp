from . import views
from django.urls import path

urlpatterns=[
path('',views.index,name='index'),
path('home',views.index,name='index'),
path('about',views.about,name='about'),
path('service',views.service,name='service'),
path('contact',views.contact,name='contact'),
path('contactcode',views.contactcode,name='contactcode'),
path('gallery',views.gallery,name='gallery')
]
