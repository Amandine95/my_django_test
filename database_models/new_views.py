"""
REST framework 提拱了两个视图基类APIView  GenericAPIView
REST的视图将继承这两个类
rest_framework.views.APIView
rest_framework.generics.GenericAPIView
"""

# 创建一个列表视图
from rest_framework.response import Response
from rest_framework.views import APIView

from database_models.models import BookInfo
from database_models.serializers import BookInfoSerializer


class BookListAPIView(APIView):
    """创建列表视图"""

    def get(self, request):
        """request是APIView中的"""

        queryset = BookInfo.objects.all()
        # 类视图用模型序列化器
        serializer = BookInfoSerializer(queryset, many=True)
        data = serializer.data
        return Response(data, status=200)
