from django.test import Client, TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from profiles.models import Profile
from pytest_django.asserts import assertTemplateUsed


class TestProfilesApp(TestCase):
    client = Client()

    def setUp(self):
        user = User.objects.create(username="user_one_username",
                                   password="password",
                                   first_name="user_one_firstname",
                                   last_name="user_one_lastname",
                                   email="user_one@gmail.com")

        Profile.objects.create(user=user,
                               favorite_city="Paris")

    def test_profiles_index_view(self):
        path = reverse('profiles:index')
        response = self.client.get(path)
        content = response.content.decode()
        assert response.status_code == 200
        assert Profile.objects.all().first().user.username in content
        assertTemplateUsed(response, 'profiles/index.html')

    def test_profiles_index_url(self):
        path = reverse('profiles:index')
        assert path == '/profiles/'
        assert resolve(path).view_name == 'profiles:index'

    def test_profiles_detail_view(self):
        profile = Profile.objects.all().first()
        path = reverse('profiles:profile', kwargs={'username': profile.user.username})
        response = self.client.get(path)
        content = response.content.decode()
        assert response.status_code == 200
        assert profile.user.username in content
        assertTemplateUsed(response, 'profiles/profile.html')

    def test_profiles_detail_url(self):
        profile = Profile.objects.all().first()
        path = reverse('profiles:profile', kwargs={'username': profile.user.username})
        assert path == '/profiles/' + profile.user.username + '/'
        assert resolve(path).view_name == 'profiles:profile'
