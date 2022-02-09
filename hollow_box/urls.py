"""hollow_box URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from article.views import ViewArticle, ViewAllArticles, CreateArticle
from user_profile.views import CreateUser, ListUsers, HelloView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/all', ViewAllArticles.as_view()),
    path('shop/<int:id>', ViewArticle.as_view()),
    path('moderator/crestearticle', CreateArticle.as_view()),
    path('moderator/createuser', CreateUser.as_view()),
    path('moderator/allusers', ListUsers.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloView.as_view(), name='hello'),
]

# nightwing@ukr.net
# BatmanSucks1404
