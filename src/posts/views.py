from inspect import Parameter
from django.shortcuts import render

# Create your views here.
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Posts
from .serializers import PostsSerializer, create_post
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from src.post_like.models import PostLike


class PostsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Posts to be viewed or edited.
    """
    queryset = Posts.objects.all()
    serializers = {'default': PostsSerializer, 'create': create_post}
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])
    
    def list(self, request):
        queryset = Posts.objects.all()
        serializer = PostsSerializer(queryset, many=True)
        
        for post in serializer.data:            
            post['liked_count'] = PostLike.objects.all().filter(liked=True, post_id=post['id']).count()
            post['unliked_count'] = PostLike.objects.all().filter(liked=False, post_id=post['id']).count()

        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'], name='get_my_posts_list')
    def get_my_posts_list(self, request, *args, **kwargs):
        data = {}
        data['user_id'] = request.user.id
        posts = Posts.objects.all().filter(**data)
        
        serialzer = PostsSerializer(posts, many=True)
        
        for post in serialzer.data:
            post['liked_count'] = PostLike.objects.all().filter(liked=True, post_id=post['id']).count()
            post['unliked_count'] = PostLike.objects.all().filter(liked=False, post_id=post['id']).count()


        return JsonResponse({'Posts': serialzer.data})
    
    
    def create(self, request):
        data = request.data
        data['user_id'] =  request.user.id
        serialzer = PostsSerializer(data=data)
        if serialzer.is_valid(raise_exception=True):
            serialzer.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)    
        
        return Response(serialzer.data, status=status.HTTP_201_CREATED)