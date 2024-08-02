"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from . import views

"""
includeを使うことで再利用性を高める。アプリごとに独立したURLパターンを
持つことでモジュール性確保
urlpatternsでDjangoプロジェクトのURLパターンを定義
URLパターンに対応するview関数をマッピング
"""

urlpatterns = [
    path('', views.index, name='index'),  # これを追加
    # Djoserによる認証のためのURL
    path("api/auth/", include("djoser.urls")),
    #DjoserのJWT認証関連のURL
    path("api/auth/", include("djoser.urls.jwt")),
    # アカウント
    path("api/", include("accounts.urls")),
    # ブログ用アプリ
    path("api/", include("app.urls")),
    # 管理画面
    path("admin/", admin.site.urls),
]