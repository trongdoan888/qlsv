from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('information', views.information, name = 'information'),

    path('api/login/', views.login, name='login_api'),

    
    
    # API Lấy chi tiết thông tin giảng viên
    path('teacher-detail/<str:id>/', views.teacher_detail, name = 'teacher_detail'),

    # API Tạo giảng viên mới
    path('api/create-teacher/', views.create_teacher, name='create_teacher_api'),
    
    # API Lấy danh sách giảng viên
    path('api/teachers/', views.get_teachers, name='get_teachers'),

    # API Xóa giảng viên
    path('api/delete_teacher/<str:id>/', views.delete_teacher, name='delete_teacher_api'),

    # API Xóa sinh viên
    path('api/delete_student/<str:id>/', views.delete_student, name='delete_student_api'),

    # API Cập nhật thông tin sinh viên
    path('api/update_student/<str:id>/', views.update_student, name='update_student_api'),

    # API Lấy danh sách sinh viên
    path('api/students/', views.get_students, name='get_students'),
    
    # API Lấy chi tiết thông tin sinh viên
    path('student-detail/<str:id>/', views.student_detail, name = 'student_detail'),

    # API Tạo sinh viên mới
    path('api/create-student/', views.create_student_api, name='create_student_api'),

    # Trang tạo sinh viên mới
    path('create-student/', views.create_student_page, name='create_student_page'),

    #Trang sửa thông tin sinh viên
    path('update_student_page/<str:id>/', views.update_student_page, name='update_student_page'),

    # Trang tạo giảng viên mới
    path('create-teacher/', views.create_teacher_page, name='create_teacher_page'),

    # Trang sửa thông tin giảng viên
    path('update_teacher_page/<str:id>/', views.update_teacher_page, name='update_teacher_page'),
    
    
]
