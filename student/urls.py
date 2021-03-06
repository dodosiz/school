from django.conf.urls import url
from . import views


urlpatterns = [
    url('^full_info/', views.full_info, name='full_info'),
    url('^basic_info/', views.basic_info, name='basic_info'),
    url('^exam_info/', views.exam_info, name='exam_info'),
    url('^financial_info', views.financial_info, name='financial_info'),
    url('^edit/(?P<student_id>[0-9]+)/', views.edit, name='edit'),
    url('^new/', views.new, name='new'),
    url('^delete/(?P<student_id>[0-9]+)/', views.delete, name='delete')
]

