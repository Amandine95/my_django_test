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
    # 序列化器添加属性,read_only 反序列化时该字段不用上传,write_only 序列化时该字段不能读取，只能反序列化时修改
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='标题', required=True, max_length=20)
    bpub_date = serializers.DateField(label='发行日期', required=True)
    bread = serializers.IntegerField(label='阅读量', required=False, default=0)
    bcomment = serializers.IntegerField(label='描述', required=False, default=0)
    is_delete = serializers.BooleanField(label='逻辑删除', write_only=True)

    # 反序列化时新建create和更新update数据模型
    def create(self, validated_data):
        """新建"""
        print('create!!!')
        # **validated_data拆包
        # return BookInfo(**validated_data)
        # 实现数据保存在数据库中
        return BookInfo.objects.create(**validated_data)

    # 调用update,需要在视图中调用反序列化器之前创建模型对象
    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        print('update!!!')
        instance.btitle = validated_data.get('btitle', instance.btitle)
        instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
        instance.bread = validated_data.get('bread', instance.bread)
        instance.bcomment = validated_data.get('bcomment', instance.bcomment)
        instance.save()
        return instance
