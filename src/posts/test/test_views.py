from django.urls import reverse
from nose.tools import ok_, eq_
from rest_framework.test import APITestCase
from rest_framework import status
from src.users.test.factories import UserFactory
from ..models import Posts

class TestCreatePosts(APITestCase):
    """
    Tests /Create Bonds detail operations.
    """

    def setUp(self):
        self.url_post = reverse('posts-list')
        # self.url_posts_list = reverse('posts_list')
        self.samle_post = {"title": "string", "description": "string"}
        self.user = UserFactory()
        tokens = self.user.get_tokens()
        access_token = tokens['access']
        self.url = reverse('user-detail', kwargs={'pk': self.user.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    def test_get_request_returns_a_given_user(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

    # def test_post_create_with_no_data_fails(self):
    #     response = self.client.post(self.url_post, {})
    #     eq_(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    # def test_posts_create_with_valid_data_succeeds(self):
    #     response = self.client.post(self.url_post, self.samle_post)
    #     eq_(response.status_code, status.HTTP_201_CREATED)
    #     eq_(response.data['title'], self.samle_post.get('title'))
    #     eq_(response.data['description'], self.samle_post.get('description'))
        
    