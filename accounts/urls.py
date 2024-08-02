from django.urls import path
from accounts import views

# accountsアプリ用のURL

urlpatterns = [
    # ユーザー詳細
    path("users/<uid>/", views.UserDetailView.as_view()),
]