from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import  giangvien, sinhvien, account
from .serializers import SinhVienSerializer, GiangVienSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import IntegrityError 
from rest_framework import status
from django.contrib.auth import authenticate, login
# Trang Login
def home(request):
    if request.method == 'POST':

        username  =  request.POST.get('username')
        password  =  request.POST.get('password')

        if username == 'admin' and password == '123':

            return redirect('information')
        
        else:
            return render(request, 'home.html', {'error': 'Tài khoản hoặc mật khẩu không hợp lệ!'})
    return render(request, 'home.html')

# Sinh Vien

# Trang chi tiết sinh viên
def student_detail(request, id):
    
    student = sinhvien.objects.get(id=id)

    return render(request, 'student_detail.html', {'student': student})

# API để lấy danh sách sinh viên
@api_view(['GET'])
def get_students(request):
    students = sinhvien.objects.all()

    serializer = SinhVienSerializer(students, many=True)

    return Response(serializer.data)

# API để tạo sinh viên mới, có xử lý lỗi khi mã sinh viên đã tồn tại
@api_view(['POST'])
def create_student_api(request):
    try:
        new_student = sinhvien.objects.create(
            name = request.data.get('name'),
            age = request.data.get('age'),
            email = request.data.get('email'),
            id = request.data.get('id'),
            lop = request.data.get('lop'),
            role = 'student'
        )

        serializers = SinhVienSerializer(new_student)
        return Response({
            'message': 'Sinh viên được tạo thành công!',
            'student': serializers.data
        }, status=201)
    except IntegrityError:
        return Response({
            'error': 'Mã sinh viên đã tồn tại. Vui lòng sử dụng mã khác.'
        }, status=400)     
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=500)

# Trang tạo sinh viên mới
def create_student_page(request):
    return render(request, 'create_student.html')

#API Xóa sinh viên
@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student = sinhvien.objects.get(id=id)
        student.delete()
        return Response({'message': 'Sinh viên đã được xóa thành công.'}, status=200)
    except sinhvien.DoesNotExist:
        return Response({'error': 'Sinh viên không tồn tại.'}, status=404)  
    
# API Cập nhật thông tin sinh viên
@api_view(['PUT'])
def update_student(request, id):
    try:
        student = sinhvien.objects.get(id=id)
    except sinhvien.DoesNotExist:
        return Response({'error': 'Sinh viên không tồn tại.'}, status=404)
    
    # Cập nhật thông tin sinh viên
    student.name = request.data.get('name', student.name)
    student.age = request.data.get('age', student.age)
    student.email = request.data.get('email', student.email)
    student.lop = request.data.get('lop', student.lop)
    student.save()

    serializer = SinhVienSerializer(student)

    return Response({
        'message': 'Thông tin sinh viên đã được cập nhật thành công.',
        'student': serializer.data
    }, status=200)

# Trang cập nhật thông tin sinh viên
def update_student_page(request, id):
    student = sinhvien.objects.get(id=id)
    return render(request, 'update_student.html', {'student': student})


# Giang Vien

# Trang chi tiết giảng viên
def teacher_detail(request, id):

    teacher = giangvien.objects.get(id=id)

    return render(request, 'teacher_detail.html', {'teacher': teacher})

#Trang tạo giảng viên mới
def create_teacher_page(request):
    return render(request, 'create_teacher.html')

# API để xóa giảng viên
@api_view(['DELETE'])
def delete_teacher(request, id):
    try:
        teacher = giangvien.objects.get(id=id)
        teacher.delete()
        return Response({'message': 'Giảng viên đã được xóa thành công.'}, status=200)
    except giangvien.DoesNotExist:
        return Response({'error': 'Giảng viên không tồn tại.'}, status=404)
    
# API để lấy danh sách giảng viên
@api_view(['GET'])
def get_teachers(request):
    teacher = giangvien.objects.all()

    serrializer = GiangVienSerializer(teacher, many=True)

    return Response(serrializer.data)

# API để tạo giảng viên mới
@api_view(['POST'])
def create_teacher_api(request):
    try:
        new_teacher= giangvien.objects.create(
            name = request.data.get('name'),
            email = request.data.get('email'),
            id = request.data.get('id'),
            khoa = request.data.get('khoa'),
            role = 'teacher'
        )

        serializers = GiangVienSerializer(new_teacher)
        return Response({
            'message': ' giảng viên được tạo thành công!',
            'student': serializers.data
        }, status=201)
    except IntegrityError:
        return Response({
            'error': 'Mã giảng viên đã tồn tại. Vui lòng sử dụng mã khác.'
        }, status=400)     
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=500)



# API để cập nhật thông tin giảng viên

@api_view(['PUT'])
def update_teacher(request, id):
    try:
        teacher = giangvien.objects.get(id=id)
    except giangvien.DoesNotExist:
        return Response({'error': 'Giảng viên không tồn tại.'}, status=404)
    
    teacher.name = request.data.get('name', teacher.name)
    teacher.email = request.data.get('email', teacher.email)
    teacher.khoa = request.data.get('major', teacher.khoa)
    teacher.save()

    serializer = GiangVienSerializer(teacher)

    return Response({
        'message': 'Thông tin giảng viên đã được cập nhật thành công.',
        'teacher': serializer.data
    }, status=200)

# Trang cập nhật thông tin giảng viên
def update_teacher_page(request, id):
    teacher = giangvien.objects.get(id=id)
    return render(request, 'update_teacher.html', {'teacher': teacher})

# Chung 
def information(request):
    students = sinhvien.objects.all()
    teachers = giangvien.objects.all()

    context = {
        'sinh_vien': students,
        'giang_vien': teachers,
        'danh_sach_tai_khoan': account.objects.all()
    }
    return render(request, 'information.html', context)

# Kiểm tra tài khoản và mật khẩu (dùng cho trang login)
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Vui lòng cung cấp tên đăng nhập và mật khẩu.'}, status=400)
    
    try:

        user_account = account.objects.get(username=username)

        if user_account.password == password:
            
            return Response({
                'message': 'Đăng nhập thành công!',
                'role': user_account.role
            }, status=200)  
        else:
            return Response({'error': 'Mật khẩu không đúng.'}, status=401)
    except account.DoesNotExist:
        return Response({'error': 'Tài khoản không tồn tại.'}, status=404)
    

# Quản lý tài khoản 

# Trang thêm tài khoản cho sinh viên hoặc giảng viên
def create_account_page(request):
    return render(request, 'create_account.html')

#api để tạo tài khoản mới cho sinh viên hoặc giảng viên
@api_view(['POST'])
def create_account(request):
    try:
        new_account = account.objects.create(
            username = request.data.get('username'),
            password = request.data.get('password'),
            role = request.data.get('role'),
            id = request.data.get('id')
        )

        user_account = account.objects.get(id=new_account.id)

        return Response({
            'message': 'Tài khoản được tạo thành công!',
            'account': {
                'username': new_account.username,
                'role': new_account.role,
                'id': new_account.id
            },
            'id_check': user_account.id
        }, status=201)
    except IntegrityError:
        return Response({
            'error': 'Tên đăng nhập đã tồn tại. Vui lòng sử dụng tên khác.'
        }, status=400)     
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=500)
    
# Trang quản lý tài khoản (có thể dùng để hiển thị danh sách tài khoản và xóa tài khoản) - chưa hoàn thiện
def manage_accounts(request):
    accounts = account.objects.all()
    return render(request, 'account_management.html', {'accounts': accounts})


# APT sửa thông tin tài khoản 
@api_view(['PUT'])
def update_account(request, id):
    try:
        user_account = account.objects.get(id=id)
    except account.DoesNotExist:
        return Response({'error': 'Tài khoản không tồn tại.'}, status=404)
    
    user_account.id = request.data.get('id', user_account.id)
    user_account.username = request.data.get('username', user_account.username)
    user_account.password = request.data.get('password', user_account.password)
    user_account.role = request.data.get('role', user_account.role)
    user_account.save()

    return Response({
        'message': 'Thông tin tài khoản đã được cập nhật thành công.',
        'account': {
            'username': user_account.username,
            'password': user_account.password,
            'role': user_account.role,
            'id': user_account.id
        }
    }, status=200)

# Trang cập nhật thông tin tài khoản
def update_account_page(request, id):
    user_account = account.objects.get(id=id)
    return render(request, 'update_account.html', {'account': user_account})

# API xóa tài khoản
@api_view(['DELETE'])
def delete_account(request, id):
    try:
        user_account = account.objects.get(id=id)
        user_account.delete()
        return Response({'message': 'Tài khoản đã được xóa thành công.'}, status=200)
    except account.DoesNotExist:
        return Response({'error': 'Tài khoản không tồn tại.'}, status=404)

#API di chuyển sinh viên và giảng viên sau khi cập nhật role

@api_view(['POST', 'PUT'])
@api_view(['POST', 'PUT'])
def move_user(request, id):
    try:
        user_account = account.objects.get(id=id)
    except account.DoesNotExist:
        return Response({'error': 'Tài khoản không tồn tại trên hệ thống.'}, status=404)
    
    new_role = request.data.get('role')  # Gồm 'student' hoặc 'teacher'

    # =========================================================================
    # TRƯỜNG HỢP 1: CHUYỂN THẲNG THÀNH SINH VIÊN ('student')
    # =========================================================================
    if new_role == 'student':
        # Kiểm tra xem mã ID này ĐÃ BỊ TRÙNG (tồn tại sẵn) bên bảng sinhvien chưa
        if sinhvien.objects.filter(id=id).exists():
            return Response({'error': f'Mã ID {id} đã tồn tại sẵn trong danh sách Sinh viên! Không thể trùng lặp.'}, status=400)
        
        # Nếu chưa trùng, tạo thẳng bản ghi mới bên bảng sinhvien không cần hỏi han bảng cũ
        sinhvien.objects.create(
            id=id,
            name=user_account.username,  # Lấy tạm tên username làm họ tên gốc
            age=20,                      # Tuổi mặc định
            email=f"{user_account.username}@gmail.com", # Email tạm thời
            lop='Chưa xếp lớp'
        )
        
        # Tiện tay xóa ngầm bên bảng giảng viên (nếu có tồn tại vết tích cũ) để làm sạch DB
        giangvien.objects.filter(id=id).delete()

    # =========================================================================
    # TRƯỜNG HỢP 2: CHUYỂN THẲNG THÀNH GIẢNG VIÊN ('teacher')
    # =========================================================================
    elif new_role == 'teacher':
        # Kiểm tra xem mã ID này ĐÃ BỊ TRÙNG (tồn tại sẵn) bên bảng giangvien chưa
        if giangvien.objects.filter(id=id).exists():
            return Response({'error': f'Mã ID {id} đã tồn tại sẵn trong danh sách Giảng viên! Không thể trùng lặp.'}, status=400)
        
        # Nếu chưa trùng, tạo thẳng bản ghi mới bên bảng giangvien (trường 'major' thay cho 'khoa')
        giangvien.objects.create(
            id=id,
            name=user_account.username,
            email=f"{user_account.username}@gmail.com",
            major='Công nghệ thông tin'
        )
        
        # Tiện tay xóa ngầm bên bảng sinh viên (nếu có tồn tại vết tích cũ)
        sinhvien.objects.filter(id=id).delete()

    # =========================================================================
    # BƯỚC CUỐI: Cập nhật lại role mới vào bảng account hệ thống
    # =========================================================================
    user_account.role = new_role
    user_account.save()

    return Response({
        'message': 'Tài khoản đã được chuyển vùng trực tiếp thành công!',
        'account': {
            'username': user_account.username,
            'role': user_account.role,
            'id': user_account.id
        }
    }, status=200)
