from django.urls import path
from myprofile import views


urlpatterns = [
    path("", views.profile, name="profile"),

]
