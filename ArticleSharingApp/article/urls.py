from django.urls import path, include
from rest_framework import routers
from .views import ArticleViewSet

routers = routers.DefaultRouter()
routers.register('articles', ArticleViewSet)

urlpatterns = [
    path('', include(routers.urls)),

]