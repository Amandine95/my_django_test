"""
自定义中间件
1,中间件作用于全局的请求前后即在请求前后做些事情
2,中间件本质是装饰器
3,根目录创建middle_ware文件,定义好中间件
4,setting.py里面的MIDDLEWARE注册中间件
"""


def my_middleware(func):
    def middleware(request):
        print('请求前操作')
        response = func(request)
        print(' 请求后操作')
        return response

    return middleware
