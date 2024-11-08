"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from task2.views import welcome, func_instance, ClassInstance
from task3.views import main, phones, amnezia
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome),
    path('path_func/', func_instance),
    path('path_class/', ClassInstance.as_view()),
    path('task3/', main, name='main'),
    path('task3/phones/', phones, name='phones'),
    path('task3/amnezia/', amnezia, name='amnezia')
]

