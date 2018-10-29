"""
定义类视图
"""
from django.http import HttpResponse
from django.views.generic import View


# 定义一个装饰器(闭包)
def my_decoration(view_func):
    def wrapper(request, *args, **kwargs):
        print('my_decoration')
        # 打印请求参数
        print(request.path)
        # 视图函数返回结果要进行返回
        return view_func(request, *args, **kwargs)


    return wrapper


# 普通视图函数添加装饰器
# @my_decoration  <=> view = my_decoration(view)
# def view(request):
#     return HttpResponse('view')


class DemoView(View):
    """自定义视图类"""

    def get(self, request):
        """get方法"""
        return HttpResponse('get')

    def post(self, request):
        """post"""
        return HttpResponse('post')
