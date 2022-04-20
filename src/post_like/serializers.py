from rest_framework import serializers
from .models import PostLike

class PostLikeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        post_like = PostLike.objects.create(**validated_data)
        return post_like

    class Meta:
        model = PostLike
        fields = '__all__'


# class create_post(serializers.ModelSerializer):
#     class Meta:
#         model = PostLike
#         fields = ['title', 'description']
