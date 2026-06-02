from rest_framework import serializers
from .models import sinhvien, giangvien

class SinhVienSerializer(serializers.ModelSerializer):
    class Meta:
        model = sinhvien
        fields = '__all__'

class GiangVienSerializer(serializers.ModelSerializer):
    class Meta:
        model = giangvien
        fields = '__all__'