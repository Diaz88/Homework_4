# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from Homework_4.hwork.models import Post
from Homework_4.hwork.models import Comment
from .serializers import PostListSerializer
from .serializers import CommentListSerializer

@api_view(['GET'])
def post_list_view(request):
    posts = Post.objects.all()
    data = PostListSerializer(posts, many=True).data
    return Response(data={'list': data})

@api_view(['GET'])
def post_item_view(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise NotFound('Товар не найден!')
    data = PostListSerializer(post).data
    return Response(data=data)

@api_view(['GET'])
def comment_view(request, id):
    comments = Comment.objects.get(id=id)
    data = CommentListSerializer(comments ).data
    return Response(data=data)