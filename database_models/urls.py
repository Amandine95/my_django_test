from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from database_models import new_views
from database_models import views

urlpatterns = [
    url(r'^modelform/$', views.ModelFormView.as_view()),

    url(r'^books/$', views.BooksAPIView.as_view()),

    url(r'^book/(?P<pk>\d+)/$', views.BookAPIView.as_view()),

    url(r'^ser/$', views.serialize),

    url(r'^deser/$', views.deserialize),

    url(r'^sers/$', views.serialize1),

    url(r'^books_api/$', new_views.BookListAPIView.as_view())
]
"""
3,创建视图集的url
"""
router = DefaultRouter()
# 注册url及视图集
router.register(r'rest_books', views.BookInfoSet)
# 路由拼接
urlpatterns += router.urls
