from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('information', views.information, name = 'information'),
    path('student-detail/<str:id>/', views.student_detail, name = 'student_detail'),
    path('teacher-detail/<str:id>/', views.teacher_detail, name = 'teacher_detail'),

    path('api/create-student/', views.create_student_api, name='create_student_api'),
    path('api/create-teacher/', views.create_teacher, name='create_teacher_api'),
    path('create-student/', views.create_student_page, name='create_student_page'),


    path('api/students/', views.get_students, name='get_students'),
    path('api/teachers/', views.get_teachers, name='get_teachers'),


    # API Xóa sinh viên
    path('api/delete_student/<str:id>/', views.delete_student, name='delete_student_api'),
    # API Cập nhật thông tin sinh viên
    path('api/update_student/<str:id>/', views.update_student, name='update_student_api'),
]
