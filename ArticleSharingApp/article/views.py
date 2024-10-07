from rest_framework.viewsets import ModelViewSet
from .models import Articles
from .serializers import ArticlesSerializer

class ArticleViewSet(ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer


