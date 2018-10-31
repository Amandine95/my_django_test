from django.conf.urls import url

from database_models import views

urlpatterns =[
    url(r'^modelform/$',views.ModelFormView.as_view()),
]