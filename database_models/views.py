import json
from datetime import datetime

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from database_models.models import BookInfo
from database_models.models_forms import MyModelForms


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
        return JsonResponse(books_list, safe=False,status=200)

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

        },status=201)


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
        return JsonResponse(book_dict,status=200)

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
        },status=202)

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
        return HttpResponse('删除成功',status=204)
