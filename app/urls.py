from django.urls import path, include
from rest_framework import routers
from app import views

router = routers.DefaultRouter() # RESTful APIのエンドポイントを生成 CRUD操作用URLパターン
router.register("posts", views.PostViewSet) # 投稿データ操作用ViewSet


urlpatterns = [
    # 投稿一覧
    path("post-list/", views.PostListView.as_view()),
    # 投稿詳細
    path("post-detail/<uid>/", views.PostDetailView.as_view()),
    # 新規、編集、削除
    path("", include(router.urls)),
]