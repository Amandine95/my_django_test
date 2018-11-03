"""
1,
REST framework实现REST API
serializers.py文件用来创建序列化器
"""
from rest_framework import serializers

from database_models.models import BookInfo


class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = '__all__'
