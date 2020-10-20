from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

# 列出所有的code snippets，或创建一个新的snippet。
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

# 获取，更新或删除一个 code snippet。
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer