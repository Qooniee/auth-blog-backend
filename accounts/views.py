from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

"""
ビューはユーザーのリクエストに基づき、対応するレスポンスを返却
ユーザーからの入力を元にモデルからデータを取得、更新し、
出力をフロント側に渡す
"""


#ユーザモデルの取得 Djangoの組み込み関数
User = get_user_model()


# ユーザー詳細ビュークラス
# RetrieveAPIViewはDRFの汎用ビュー　あるオブジェクトの詳細情報を取得する
class UserDetailView(RetrieveAPIView):
    # ビューが操作するデータセットの指定 全てのユーザーオブジェクトを対象
    queryset = User.objects.all()
    # シリアライザクラスの指定 ユーザオブジェクトのシリアライズ
    serializer_class = UserSerializer
    # ビューにアクセスするためのpermission 認証されてないユーザーも含む全てのユーザーを許可
    permission_classes = (AllowAny,)
    # URLで使用されるオブジェクトの識別フィールド
    # http://example.com/users/<uid>/ のように <uid> がユーザーを特定するための
    # フィールドとして使われる
    lookup_field = "uid"