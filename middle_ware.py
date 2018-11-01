"""
自定义中间件
1,中间件作用于全局的请求前后即在请求前后做些事情
2,中间件本质是装饰器
3,根目录创建middle_ware文件,定义好中间件
4,settings.py里面的MIDDLEWARE注册中间件
"""


def my_middleware(func):
    def middleware(request):
        print('请求前操作')
        response = func(request)
        print(' 请求后操作')
        return response

    return middleware


"""
中间件执行流程：
1,装饰顺序按照settings.py里面的注册顺序
2,执行流程和多装饰器相同
3,  请求前操作
    请求前操作2

    视图函数执行操作

    请求后操作2
    请求后操作

"""


def my_middleware2(func):
    def middleware(request):
        print('请求前操作2')
        response = func(request)
        print(' 请求后操作2')
        return response

    return middleware
