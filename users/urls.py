from django.conf.urls import url

from . import views
# 路由列表变量
urlpatterns = [
    # url函数构造路由信息
    # url(路径，视图)
    url(r'^index/$', views.index,name='index'),

    # 路由解析顺序(下面这种写法会出现路由屏蔽)
    url(r'^say/$',views.say,name='say'),
    # 普通路由的名字 name
    #   /  作用是访问  sayhello/  和 sayhello  都会到同样视图函数
    url(r'^sayhello/$',views.sayhello,name='sayhello')

]
