from django.test import Client, TestCase
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed


class TestHome(TestCase):
    client = Client()

    def test_home_view(self):
        path = reverse('home')
        response = self.client.get(path)
        assert response.status_code == 200
        assertTemplateUsed(response, 'index.html')

    def test_home_url(self):
        path = reverse('home')
        assert path == '/'
        assert resolve(path).view_name == 'home'
