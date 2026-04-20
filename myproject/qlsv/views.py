from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import  giangvien, sinhvien
from .serializers import SinhVienSerializer, GiangVienSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
def student_detail(request, id):
    
    student = sinhvien.objects.get(id=id)

    return render(request, 'student_detail.html', {'student': student})

@api_view(['GET'])
def get_students(request):
    students = sinhvien.objects.all()

    serializer = SinhVienSerializer(students, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def create_student(request):
    new_student = sinhvien.objects.create(
        name = request.data.get('name'),
        age = request.data.get('age'),
        email = request.data.get('email'),
        id = request.data.get('id'),
        lop = request.data.get('lop')
    )
    serializers = SinhVienSerializer(new_student)
    return Response(serializers.data)

# Giang Vien
def teacher_detail(request, id):

    teacher = giangvien.objects.get(id=id)

    return render(request, 'teacher_detail.html', {'teacher': teacher})

@api_view(['GET'])
def get_teachers(request):
    teacher = giangvien.objects.all()

    serrializer = GiangVienSerializer(teacher, many=True)

    return Response(serrializer.data)

@api_view(['POST'])
def create_teacher(request):
    serializer = SinhVienSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# Chung 
def information(request):
    students = sinhvien.objects.all()
    teachers = giangvien.objects.all()

    context = {
        'sinh_vien': students,
        'giang_vien': teachers
    }
    return render(request, 'information.html', context)





