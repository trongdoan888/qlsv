from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import giangvien, sinhvien, account
from ..serializers import SinhVienSerializer, GiangVienSerializer
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework import status
from django.contrib.auth import authenticate, login
import random
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from ..helpers.basic_authentication import basic_auth_required

# Trang chi tiết sinh viên
def student_detail(request, id):

    student = sinhvien.objects.get(id=id)

    return render(request, "student_detail.html", {"student": student})

# Trang tạo sinh viên mới
def create_student_page(request):
    return render(request, "create_student.html")

# Trang cập nhật thông tin sinh viên
def update_student_page(request, id):
    student = sinhvien.objects.get(id=id)
    return render(request, "update_student.html", {"student": student})

# API để lấy danh sách sinh viên
@api_view(["GET"])
def get_students(request):
    students = sinhvien.objects.all()

    serializer = SinhVienSerializer(students, many=True)

    return Response(serializer.data)
