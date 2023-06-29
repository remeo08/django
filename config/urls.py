"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from boards import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/users/', include("users.urls")),
    path('api/v1/boards/', include("boards.urls")),   # 파일의 경로 - html
    path('api/v1/reviews/', include("reviews.urls")),
    path('api/v1/users/', include("users.urls")),
    # path('api/v2/users/', include("users.urls")),     # v1, v2 버전을 만드는 이유: 웹은 업데이트가 바로 적용을 하니까 별 의미가 없긴 하지만 앱 로그인을 업데이트했다치면 버전1을 쓰는 사람은 로그인 자체가 안될테니 v1을 계속 사용할 수 있도록 하는 것
    # path('api/v2/board/', include("boards.urls")),
    # path('board/',views.show_board),
    # path('board/all', views.all_board),
]
