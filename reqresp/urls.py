from django.conf.urls import url

from . import views

urlpatterns = [
    # 1,正则匹配路由，()分组 传递参数,分别对应视图中的除了 request 外的其他参数   接受参数必须按顺序
    # url(r'weather/([a-z]+)/(\d{4})/$', views.request_para),

    # 2,路由中给参数命名  正则的命名法  ?P<name>命名    命名放在()分组里    接受参数顺序不限
    url(r'weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.request_para),

]
