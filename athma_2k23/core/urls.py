from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('error', views.error, name='error'),
    path('team', views.team, name='team'),
    path('signup', views.signup, name="signup"),
    path('signin',views.signin, name="signin"),
    path('logout',views.logout, name="logout"),
]