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
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from ..helpers.basic_authentication import basic_auth_required

# API để tạo sinh viên mới, có xử lý lỗi khi mã sinh viên đã tồn tại
@api_view(["POST"])
def create_student_api(request):
    try:
        new_student = sinhvien.objects.create(
            name=request.data.get("name"),
            age=request.data.get("age"),
            email=request.data.get("email"),
            id=request.data.get("id"),
            lop=request.data.get("lop"),
            role="student",
        )

        serializers = SinhVienSerializer(new_student)
        return Response(
            {"message": "Sinh viên được tạo thành công!", "student": serializers.data},
            status=201,
        )
    except IntegrityError:
        return Response(
            {"error": "Mã sinh viên đã tồn tại. Vui lòng sử dụng mã khác."}, status=400
        )
    except Exception as e:
        return Response({"error": str(e)}, status=500)

# API Xóa sinh viên
@basic_auth_required
@api_view(["DELETE"])
def delete_student(request, id):
    try:
        student = sinhvien.objects.get(id=id)
        student.delete()
        return Response({"message": "Sinh viên đã được xóa thành công."}, status=200)
    except sinhvien.DoesNotExist:
        return Response({"error": "Sinh viên không tồn tại."}, status=404)

# API Cập nhật thông tin sinh viên
@api_view(["PUT"])
def update_student(request, id):
    student = get_object_or_404(sinhvien, id=id)
    update_form = SinhVienSerializer(instance=student, data=request.data, partial=True)

    if not update_form.is_valid():
        return Response(
            {
                "message": "Thông tin không đúng định dạng.",
            },
            status=401,
        )
    update_form.save()
    return Response(
        {
            "message": "Thông tin sinh viên đã được cập nhật thành công.",
            "student": update_form.data,
        },
        status=200,
    )