from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('student-information', views.student_information, name = 'student_information'),
    path('student-detail/<str:student_id>/', views.student_detail, name = 'student_detail'),
    path('teacher-detail/<str:teacher_id>/', views.teacher_detail, name = 'teacher_detail'),
]
