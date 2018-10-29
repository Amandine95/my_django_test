import json

from django.http import HttpResponse


def request_para(request, city, year):
    """
    请求参数
    city,year 分别对应正则匹配出来的 路由中的参数，按顺序的
    """
    print(city)
    print(year)

    # # 获取查询参数(url里用 ? 拼接),request 的GET 属性 可以获取查询参数
    # # url: weather/shanghai/2018/?a=1&b=2&a=3   适用于get/post/put等请求方式
    # a = request.GET.get('a')
    # b = request.GET.get('b')
    # # 获取同名参数列表
    # a_list = request.GET.getlist('a')
    # b_list = request.GET.getlist('b')
    # # 不存在返回空列表
    # c_list = request.GET.getlist('c')
    # print(a)
    # print(b)
    # print(a_list)
    # print(b_list)
    # print(c_list)
    # print('-' * 20)

    # 获取请求体参数，如果有同名参数，那么获取的是同名参数的最后一个值
    # post 只能获取 普通 表单格式 的 请求体 的参数
    d = request.POST.get('d')
    e = request.POST.get('e')
    d_list = request.POST.getlist('d')
    print(d)
    print(e)
    print(d_list)
    print('*' * 10)

    # # 非表单格式请求体，用body获取 返回bytes类型
    # json_bytes = request.body
    # # json.loads() 在 py3.6 接收 str,bytes   py3.5 接收 str(因此需要将body获取的参数解码)
    # req_dict = json.loads(json_bytes.decode())
    # # 从字典获取参数
    # f = req_dict.get('f')
    # g = req_dict.get('g')
    # print(f)
    # print(g)

    return HttpResponse('ok')


def response_test(request):
    """构造响应"""

    # # 默认响应头
    # result = '{"name": "sam"}'
    # # 三个参数  content  content_type status
    # return HttpResponse(content=result, content_type="application/json", status=400)

    # 构造自定义响应头
    response = HttpResponse()
    response["name"] = "sam"
    # 设置响应头属性
    response.content = '{"type":"python"}'
    response._content_type = "application/json"
    response.status_code = 400

    # 设置session
    request.session["name"] = "bily"
    request.session["age"] = 20

    return response
