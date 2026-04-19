from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('student-information', views.information, name = 'information'),
    path('student-detail/<str:id>/', views.student_detail, name = 'student_detail'),
    path('teacher-detail/<str:id>/', views.teacher_detail, name = 'teacher_detail'),
    path('api/students/', views.get_students, name='get_students'),
    path('api/teachers/', views.get_teachers, name='get_teachers'),
]
