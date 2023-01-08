from django.urls import path, include
from . import views

app_name = "main"

urlpatterns = [
	path('', views.index, name="home"),
	path('results', views.results, name="results"),
	path('signin',views.signin,name='signin'),
	path('signup',views.signup,name='signup'),
	path('action',views.action,name='action'),
	path('invalid',views.invalid,name='invalid'),
	 path('logout',views.logout,name='logout'),

]


