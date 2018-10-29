"""
定义类视图
"""
from django.http import HttpResponse
from django.views.generic import View


class DemoView(View):
    """自定义视图类"""

    def get(self, request):
        """get方法"""
        return HttpResponse('get')

    def post(self, request):
        """post"""
        return HttpResponse('post')
