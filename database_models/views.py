import json
from datetime import datetime

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.viewsets import ModelViewSet

from database_models.models import BookInfo
from database_models.models_forms import MyModelForms
from database_models.serializers import BookInfoSerializer, BookInfoSerializer2


class ModelFormView(View):
    """表单视图"""

    def get(self, request):
        """渲染模板，将表单对象发给模板"""
        form1 = MyModelForms()
        context = {
            "form1": form1
        }
        return render(request, 'forms_template.html', context)

    def post(self, request):
        """对表单提交进行处理"""
        # 获取参数,POST属性获取表单参数
        form1 = MyModelForms(request.POST)
        # 校验通过
        if form1.is_valid():
            # 获取表单数据
            print(form1.cleaned_data)
            return HttpResponse('ok')
        else:
            # 渲染模板,django提供了错误信息提示
            return render(request, 'forms_template.html', context={"form1": form1})


"""
实现一个REST接口的定义
1,前后端分离
2,路由定义遵循REST规范
3,前后端以JSON格式传递数据
"""


class BooksAPIView(View):
    """
    图书API
    """

    def get(self, request):
        """
        查询所有数据
         url   GET/books/
        """
        books = BookInfo.objects.all()
        books_list = []
        for book in books:
            books_list.append({
                "pk": book.pk,
                "title": book.btitle,
                "pubdate": book.bpub_date,
                "read": book.bread,
                "comment": book.bcomment,
                "is_delete": book.is_delete

            })
        # safe为True时确保传入的是字典
        return JsonResponse(books_list, safe=False, status=200)

    def post(self, request):
        """
        添加数据
        url  POST/books/
        """
        # josn格式的数据用body接收,接收到的是bytes格式数据
        json_bytes = request.body
        json_str = json_bytes.decode()
        # json.loads 将json转化为字典
        json_dict = json.loads(json_str)
        book = BookInfo.objects.create(
            btitle=json_dict.get("btitle"),
            # 日期在数据库以日期对象存储， strptime  日期字符串转为对象
            bpub_date=datetime.strptime(json_dict.get("bpub_date"), "%Y-%m-%d").date()
        )
        # 请求成功，按照REST规则，将接收到的数据返回前端
        return JsonResponse({
            "pk": book.pk,
            "title": book.btitle,
            "pubdate": book.bpub_date,
            "read": book.bread,
            "comment": book.bcomment,
            "is_delete": book.is_delete

        }, status=201)


class BookAPIView(View):
    """对单个数据的处理"""

    def get(self, request, pk):
        """
        获取单个
        参数: pk(id),request
        url:  GET/book/pk  (正则设置路由)
        """
        # pk通过url传递
        if not pk:
            return HttpResponse(status=404)
        try:
            pk = int(pk)
        except Exception as e:
            return HttpResponse(status=404)
        try:
            book = BookInfo.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=404)
        book_dict = {
            "pk": book.pk,
            "title": book.btitle,
            "pubdate": book.bpub_date,
            "read": book.bread,
            "comment": book.bcomment,
            "is_delete": book.is_delete
        }
        return JsonResponse(book_dict, status=200)

    def put(self, request, pk):
        """
        修改单个数据
        参数: request,pk
        url: PUT/book/pk
        """
        if not pk:
            return HttpResponse(status=404)
        try:
            pk = int(pk)
        except Exception as e:
            return HttpResponse(status=404)
        try:
            book = BookInfo.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=404)
        # 获取参数
        json_bytes = request.body
        json_str = json_bytes.decode()
        json_dict = json.loads(json_str)
        book.btitle = json_dict.get("btitle")
        book.bpub_date = datetime.strptime(json_dict.get("bpub_date"), "%Y-%m-%d").date()
        book.save()
        return JsonResponse({
            "pk": book.pk,
            "title": book.btitle,
            "pubdate": book.bpub_date,
            "read": book.bread,
            "comment": book.bcomment,
            "is_delete": book.is_delete
        }, status=202)

    def delete(self, request, pk):
        """
        删除单个数据
        参数: request,pk
        url: DELETE/book/pk
        """
        if not pk:
            return HttpResponse(status=404)
        try:
            pk = int(pk)
        except Exception as e:
            return HttpResponse(status=404)
        try:
            book = BookInfo.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=404)
        book.delete()
        return HttpResponse('删除成功', status=204)


"""
2,REST framework 创建视图集
"""


class BookInfoSet(ModelViewSet):
    """图书视图集"""
    # 所有图书信息的查询结果集
    queryset = BookInfo.objects.all()
    # 指明序列化器
    serializer_class = BookInfoSerializer


"""
创建视图函数 模拟序列化/反序列化
初始化后的序列器对象参数：instance(序列化时，传入模型数据),data(反序列化时，传入接收到的前端数据)
"""


def serialize(request):
    """序列化"""
    # 查询数据库
    book = BookInfo.objects.get(id=1)
    # 序列化
    ser = BookInfoSerializer2(book)
    print(ser.data)
    return HttpResponse('序列化成功%s' % ser.data)


def deserialize(request):
    """反序列化"""
    # 模拟接收到的数据
    data = {
        "btitle": "数学",
        "bpub_date": "1999-09-09",
        "bread": 100,
        "is_delete": 0
    }
    # 接收到的数据传入data参数
    deser = BookInfoSerializer2(data=data)
    # 校验结果
    print(deser.is_valid())
    # 返回错误信息
    print(deser.errors)
    # 清洗后数据,为空返回{}
    print(deser.validated_data)

    return HttpResponse('反序列化结束%s' % deser.validated_data)


def serialize1(request):
    """多条序列化"""
    # 查询数据库
    bookset = BookInfo.objects.all()
    # 多条序列化,添加属性many
    ser = BookInfoSerializer2(bookset, many=True)
    print(ser.data)
    return HttpResponse('序列化成功%s' % ser.data)
