"""landingpage URL Configuration

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
from django.contrib import admin
from django.urls import path
from main.views import index # main안에 views의 index 함수를 매칭
from django.conf.urls.static import static # 이미지 경로
from django.conf import settings           # 불어오기 

urlpatterns = [
    path('admin/', admin.site.urls), # path =  https://python-games-epshm.run.goorm.io/admin
    path('', index), # path =  https://python-games-epshm.run.goorm.io
]

# 등록된 이미지 보여주는 url
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)