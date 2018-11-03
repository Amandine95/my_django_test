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
    # 字段添加限制,read_only 反序列化时该字段不用上传,write_only 序列化时该字段不能读取，只能反序列化时修改
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='标题', required=True, max_length=20)
    bpub_date = serializers.DateField(label='发行日期', required=True)
    bread = serializers.IntegerField(label='阅读量', required=False, default=0)
    bcomment = serializers.IntegerField(label='描述', required=False, default=0)
    is_delete = serializers.BooleanField(label='逻辑删除', write_only=True)
