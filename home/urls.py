from django.urls import path

from . import views
from home.views import myhome

urlpatterns = [
    path('', views.index, name='index'),
    path('includes/planning.html', views.myhome, name='planning'),
]
