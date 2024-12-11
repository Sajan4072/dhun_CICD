"""MusicClassification URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'predictor'

urlpatterns = [
    path('',views.log,name='log'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('register/',views.registerPage,name='register'),
    path('blogs',views.blogs,name='blogs'),
    path('about',views.about,name='about'),
    path('add',views.add,name='add'),
    path('post',views.post,name='post'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('index', views.IndexView.as_view(), name='index'),
    path('result/',views.model_form_upload,name = 'result'),
]
