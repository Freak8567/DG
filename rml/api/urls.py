from django.conf.urls import url
from api import views

urlpatterns = [
	url(r'^save/$', views.save_data ,name='save_data'),     
]