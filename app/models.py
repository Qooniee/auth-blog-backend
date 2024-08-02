from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from hashids import Hashids
from django.core.exceptions import ValidationError

def validate_isbn_length(isbn_value):
    if len(isbn_value) not in [10, 13]:
        raise ValidationError(
            f'ISBN length must be either 10 or 13 characters Got {len(isbn_value)} characters.'
        )


# 投稿モデル DBテーブルをPython Classで定義
class Post(models.Model):
    uid = models.CharField("uid", max_length=30, unique=True) # Post ID 投稿が作成された後にUIDを生成
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="ユーザー", on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to="post", verbose_name="サムネイル", null=True, blank=True
    )
    #isbn = models.CharField("isbn", max_length=10, null=False, blank=False, default="None")
    isbn = models.CharField(
        "isbn",
        max_length=13,
        null=False,
        blank=False,
        default="None",
        validators=[validate_isbn_length]
    )
    title = models.CharField("タイトル", max_length=255)
    author = models.CharField("著者", max_length=32,  null=False, blank=False, default="None")
    content = models.TextField("感想")
    updated_at = models.DateTimeField("更新日", auto_now=True)
    created_at = models.DateTimeField("作成日", auto_now_add=True)

    class Meta:
        verbose_name = "投稿"
        verbose_name_plural = "投稿"

    def __str__(self):
        return self.title


# 投稿が保存された後に実行されるシグナルレシーバー
@receiver(post_save, sender=Post)
def generate_random_post_uid(sender, instance, created, **kwargs):
    # 新規作成時にランダムUIDを生成
    if created:
        hashids = Hashids(salt="xRXSMT8XpzdUbDNM9qkv6raerwre3223", min_length=8)
        instance.uid = hashids.encode(instance.id)
        instance.save()