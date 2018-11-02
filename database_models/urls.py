from django.conf.urls import url

from database_models import views

urlpatterns = [
    url(r'^modelform/$', views.ModelFormView.as_view()),

    url(r'^books/$', views.BooksAPIView.as_view()),

    url(r'^book/(?P<pk>\d+)/$', views.BookAPIView.as_view())
]
