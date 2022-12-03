from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home-page'),
    path('about', about_us, name='about-page'),
    path('contact/', contact, name='contact'),
    path('newsletter/', newsletter, name='newsletter'),
    path('student/add', student_add, name='student-add'),
    path('student-detail/<pk>',student_detail, name='student-detail'),
    path('student-update/<pk>',student_update, name='student-update'),
    path('student-delete/<pk>',student_delete, name='student-delete'),

    # CBV
    path('teacher', TeacherList.as_view(), name='teacher'),
    path('teacher/<pk>/detail', TeacherDetail.as_view(), name='teacher-detail'),
    path('add/new/teacher', TeacherAdd.as_view(template_name = 'teacher-add.html'), name='teacher-add'),
    path('teacher/<pk>/information/update', TeacherUpdate.as_view(template_name = 'teacher-add.html'), name='teacher-update'),
    path('teacher/<pk>/information/delete', TeacherDelete.as_view(), name='teacher-delete'),

]