from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^student/(?P<pk>\d+)$', views.StudentModifyView, name='student-detail'),
    # re_path('student/(?P<pk>\d+)', views.StudentDetailView.as_view(), name='student-detail'),
    path('student/create/', views.StudentCreate, name='student-create'),
    re_path('^student/operation/$', views.StudentModifyDelete, name='student-operation'),
    re_path('^student/find/(?P<keyword>\S+)$', views.StudentFind, name='student-find'),
    path('', views.index, name='index'),
    re_path('(?P<page>\d+)', views.index, name='index-slice'),
]
