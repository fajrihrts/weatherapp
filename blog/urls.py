from django.contrib import admin
from django.urls import path, include
from WeatherApp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('weather/', views.weather, name="weather"),
    path('delete/<CName>', views.delete_city, name="DCity"),
    path('login/', views.login, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace='social')),
    
]
