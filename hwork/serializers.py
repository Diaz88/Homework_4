from rest_framework import serializers
from .models import Post
from .models import Comment

class CommentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'id text '.split()

class PostListSerializer(serializers.ModelSerializer):
    comments = CommentItemSerializer(many=True)
    comments_count = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = 'id title created_date comments comments_count'.split()

    def get_comments_count(self, obj):
            return obj.comments.count()

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
