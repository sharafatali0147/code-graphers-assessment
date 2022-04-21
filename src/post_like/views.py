from django.shortcuts import render
from rest_framework import viewsets
from .models import PostLike
from .serializers import PostLikeSerializer, create_postLike
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class PostLikeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PostLike to be viewed or edited.
    """
    queryset = PostLike.objects.all()
    serializers = {'default': PostLikeSerializer, 'create': create_postLike}
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post']
    
    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])
    
    def create(self, request):
        data = request.data
        data['liked_by'] = request.user.id
        post_like = PostLike.objects.all().filter(**data)
        if post_like:
            return Response("already done", status=status.HTTP_208_ALREADY_REPORTED)
        
        serialzer = PostLikeSerializer(data=data)
        
        if serialzer.is_valid(raise_exception=True):
            serialzer.save()
        else:
            return Response(status=401)    
        
        return Response(serialzer.data, status=status.HTTP_201_CREATED)