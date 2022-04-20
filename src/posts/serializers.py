from rest_framework import serializers
from .models import Posts

class PostsSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        posts = Posts.objects.create(**validated_data)
        return posts

    class Meta:
        model = Posts
        fields = '__all__'


class create_post(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['title', 'description']
