from rest_framework import serializers
from posts.models import Post


class PostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'vin', 'head', 'user')


class PostDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'
