from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main, name='main_page'),
    url(r'(?P<expert_id>[0-9]+)/validation/$', views.validation, name='validation_page')
]