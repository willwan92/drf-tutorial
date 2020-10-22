from django.urls import path, include
from snippets import views
from rest_framework.routers import DefaultRouter

# 创建路由器并注册我们的视图。
# 使用的DefaultRouter类也会自动为我们创建API根视图
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# API URL现在由路由器自动确定。
urlpatterns = [
    path('', include(router.urls)),
]