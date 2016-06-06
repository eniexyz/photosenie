from django.conf.urls import url

from . import views

app_name = 'photos'

urlpatterns = [
	url(r'^$', views.sign_up, name='sign-up'),
]