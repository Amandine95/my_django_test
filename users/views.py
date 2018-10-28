from django.http import HttpResponse
from django.urls import reverse


def index(request):
    """
    index
    :param request:请求对象
    :return: 响应对象
    """
    return HttpResponse('hello world!!')


def say(request):
    # reverse 根据路由名返回路径
    url=reverse('users:say')
    print(url)
    return HttpResponse('say')


def sayhello(request):
    return HttpResponse('sayhello')