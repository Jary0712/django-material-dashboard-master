from django.urls import path

from . import views
from home.views import myhome

urlpatterns = [
    path('', views.index, name='index'),
    path('includes/kanban.html', views.myhome, name='kanban'),
]
