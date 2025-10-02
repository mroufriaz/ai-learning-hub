from django.urls import path

from . import views




urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('resources/', views.resources, name='resources'),
    path('contact-us/', views.contact, name='contact'),
    path('about-us/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),

]

