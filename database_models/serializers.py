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


"""
创建序列化器进行序列化/反序列化操作
序列化器独立于模型外
继承于 serializers.Serializer
"""


class BookInfoSerializer2(serializers.Serializer):
    """序列化器2"""

    # 添加需要序列化的字段,类型参考数据库模型
    # 这里的命名和数据模型相同，不然报错
    id = serializers.IntegerField()
    btitle = serializers.CharField()
    bpub_date = serializers.DateField()
    bread = serializers.IntegerField()


