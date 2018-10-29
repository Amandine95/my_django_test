"""
定义类视图
"""
from django.http import HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator


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
"""
类视图/类视图方法添加装饰器都要 method_decorator
"""


class DemoView(View):
    """自定义视图类"""

    @method_decorator(my_decoration)
    def dispatch(self, request, *args, **kwargs):
        """重写父类方法,所有请求方式都会调用这个方法"""
        return super().dispatch(request, *args, **kwargs)

    # @method_decorator(my_decoration) 给单独的方法添加装饰器
    def get(self, request):
        """get方法"""
        return HttpResponse('get')

    def post(self, request):
        """post"""
        return HttpResponse('post')
