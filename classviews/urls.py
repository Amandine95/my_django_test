from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^classview/$', views.DemoView.as_view())

]
