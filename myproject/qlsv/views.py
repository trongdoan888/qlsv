from urllib import request

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def student_information(request):
    thong_tin_sinh_vien = [
        {
        'id': 'PH12345',
        'name': 'Nguyen Van A',
        'age': 20,
        'lop': 'CTK42'
        },
         {
        'id': 'PH235525',
        'name': 'Nguyen Van B',
        'age': 24,
        'lop': 'CTK42'
        },
         {
        'id': 'PH7463',
        'name': 'Nguyen Van C',
        'age': 67,
        'lop': 'CTK42'
        },
    ]

    thong_tin_giang_vien = [
        {'id': 'GV12345',
        'name': 'Nguyen Anh Quân',
        'major': 'Công nghệ thông tin',
        },
        {'id': 'GV235525',
        'name': 'Nguyen Van B', 
        'major': 'Công nghệ thông tin',
        },
        {'id': 'GV7463',
        'name': 'Nguyen Van C',
        'major': 'Công nghệ thông tin',
        }, 
    ]

    context = {
        'sinh_vien': thong_tin_sinh_vien,
        'giang_vien': thong_tin_giang_vien
    }
    return render(request, 'student_information.html', context) 

def home(request):
    if request.method == 'POST':

        username  =  request.POST.get('username')
        password  =  request.POST.get('password')

        if username == 'admin' and password == '123':

            return redirect('student_information')
        
        else:
            return render(request, 'home.html', {'error': 'Tài khoản hoặc mật khẩu không hợp lệ!'})
    return render(request, 'home.html')

def student_detail(request, student_id):

    
    return HttpResponse(f'Student Detail Page - Student ID: {student_id}')

def teacher_detail(request, teacher_id):
    
    return HttpResponse(f'Teacher Detail Page - Teacher ID: {teacher_id}')



