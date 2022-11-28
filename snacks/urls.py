from .views import Homepageview, Aboutpageview
from django.urls import path


urlpatterns = [
    path('', Homepageview.as_view(), name='home'),
    path('about', Aboutpageview.as_view(), name='about'),
]