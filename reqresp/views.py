from django.http import HttpResponse


def request_para(request, city, year):
    """
    请求
    city,year 分别对应正则匹配出来的 路由中的参数，按顺序的
    """
    print(city)
    print(year)
    return HttpResponse('ok')
