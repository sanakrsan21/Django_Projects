from django.urls import path
from accounts import views
from django.conf.urls import url

app_name = 'accounts'

urlpatterns=[
    url('register',views.register, name='register'),
    url('userdtl/',views.userdtl,name='userdtl'),
]