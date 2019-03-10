from django.urls import path, re_path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('(?P<result>\S+)', views.index_plus, name='index-plus'),
    re_path('student/(?P<pk>\d+)', views.StudentDetailView.as_view(), name='student-detail'),
    path('student/create/', views.StudentCreate, name='student-create'),
    re_path('student/operation/', views.StudentModifyDelete, name='student-operation'),
]
