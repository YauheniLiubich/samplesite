from django.urls import path

from . import views
from .views import by_rubric, BbCreateView

urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', views.index, name='index'),
]
