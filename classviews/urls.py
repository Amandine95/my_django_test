from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^classview/$', views.DemoView.as_view())

    # url添加装饰器
    url(r'^classview/$',views.my_decoration(views.DemoView.as_view()))
]
