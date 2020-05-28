from django.urls import path

from . import views
from .views import by_rubric

urlpatterns = {
    path('<int:rubric_id>', by_rubric),
    path('', views.index, name='index'),
}
