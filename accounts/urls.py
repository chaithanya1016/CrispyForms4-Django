from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup_view, name="signup"),

]
