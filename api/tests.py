from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from posts.models import Follow

User = get_user_model()


class TestCaseBase(APITestCase):
    @property
    def bearer_token(self):
        user = User.objects.create_user(
            username='test_user', password='12345678'
        )

        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh.access_token}'}


class PostsTestClass(TestCaseBase):

    def test_get_posts(self):
        """Список постов"""
        response = self.client.get(reverse('posts-list'), **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_posts(self):
        """Создание поста"""
        data = {"title": "Tets_title", "text": "Test_text"}
        response = self.client.post(
            reverse('posts-list'), data,
            **self.bearer_token
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class PostsListTestClass(TestCaseBase):

    def test_get_posts(self):
        """Страница с постами подписок"""
        response = self.client.get(
            reverse('posts-list-list'),
            **self.bearer_token
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class FollowTestClass(TestCaseBase):
    def test_get_follow(self):
        """Список подписок"""
        response = self.client.get(reverse('follow-list'), **self.bearer_token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_follow(self):
        """Подписка на пользователя"""
        User.objects.create_user(
            username="Maxim", password='12345678'
        )
        data = {"following": "Maxim"}
        response = self.client.post(
            reverse('follow-list'),
            data,
            **self.bearer_token
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)




