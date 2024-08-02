
from django.http import HttpResponse

def index(request):
    return HttpResponse("ようこそ！このサイトはDjangoで作られたAPIサーバーです。")

