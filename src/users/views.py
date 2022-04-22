from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from src.services.getIP import get_client_ip
from src.services.abstractapi import get_IP_geolocation, email_validate
from src.users.models import User
from src.users.permissions import IsUserOrReadOnly
from src.users.serializers import CreateUserSerializer, UserSerializer
from src.geolocation.serializers import GeolocationSerializer
from rest_framework.exceptions import APIException



class UserViewSet(viewsets.ModelViewSet):
    """
    Creates, Updates and Retrieves - User Accounts
    """

    queryset = User.objects.all()
    serializers = {'default': UserSerializer, 'create': CreateUserSerializer}
    permissions = {'default': (IsUserOrReadOnly,), 'create': (AllowAny,)}
    
    def create(self, request):
        data = request.data
        try:
            data['username'] =  data['email']
        except:
            raise APIException("Email is required!")
        valid_email = email_validate(data['email'])
        
        if valid_email and valid_email['deliverability'] != "DELIVERABLE":
            raise APIException("Email is not DELIVERABLE!")
        
        serialzer = CreateUserSerializer(data=data)
        if serialzer.is_valid(raise_exception=True):
            serialzer.save()
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)    
        holiday, geolocation_dict = get_IP_geolocation(ip_address=get_client_ip(self.request))
        
        geo_data = {}
        geo_data['user_id'] =  serialzer.data['id']
        geo_data['user_geolocation'] =  geolocation_dict
        geo_data['holidays'] =  holiday
        
        geo_serialzer = GeolocationSerializer(data=geo_data)
        if geo_serialzer.is_valid(raise_exception=True):
            geo_serialzer.save()
        
        return Response(serialzer.data, status=status.HTTP_201_CREATED)

    
    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.permissions['default'])
        return super().get_permissions()

    @action(detail=False, methods=['get'], url_path='me', url_name='me')
    def get_user_data(self, instance):
        try:
            return Response(UserSerializer(self.request.user, context={'request': self.request}).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Wrong auth token' + e}, status=status.HTTP_400_BAD_REQUEST)


