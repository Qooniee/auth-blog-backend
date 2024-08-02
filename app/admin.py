from django.contrib import admin
from django.contrib.admin import ModelAdmin
from app.models import Post

# 投稿するモデルを管理画面で操作可能にする
class PostCustom(ModelAdmin):
    # 一覧
    list_display = ("uid", "user", "isbn", "title", "author", "updated_at", "created_at")
    # リンク
    list_display_links = ("uid", "user", "title")
    # 順番
    ordering = ("-updated_at",)
    # 編集不可
    readonly_fields = ("uid", "updated_at", "created_at")


admin.site.register(Post, PostCustom)