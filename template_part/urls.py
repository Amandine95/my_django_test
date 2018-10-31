from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^template/$',views.TemplateView.as_view()),
]