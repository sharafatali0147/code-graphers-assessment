from rest_framework import serializers
from .models import Posts

class PostsSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        posts = Posts.objects.create(**validated_data)
        return posts

    class Meta:
        model = Posts
        fields =  ['id', 'title', 'description', 'liked_count', 'unliked_count', 'user_id', 'created_at', 'updated_at']
        
        extra_kwargs = {"liked_count": {"required": False, "allow_null": True}, "unliked_count": {"required": False, "allow_null": True}}


class create_post(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['title', 'description']
