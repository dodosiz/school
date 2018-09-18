from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.students_view, name='index')
]