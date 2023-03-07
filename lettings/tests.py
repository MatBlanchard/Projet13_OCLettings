from django.test import Client, TestCase
from django.urls import reverse, resolve
from lettings.models import Letting, Address
from pytest_django.asserts import assertTemplateUsed


class TestLettingsApp(TestCase):
    client = Client()

    def setUp(self):
        address = Address.objects.create(number=99,
                                         street='Avenue des Champs-Élysées',
                                         city='Paris',
                                         state='Paris',
                                         zip_code=75008,
                                         country_iso_code='FRA')

        Letting.objects.create(title='Fouquets',
                               address=address)

    def test_lettings_index_view(self):
        path = reverse('lettings:index')
        response = self.client.get(path)
        content = response.content.decode()
        assert response.status_code == 200
        assert Letting.objects.all().first().title in content
        assertTemplateUsed(response, 'lettings/index.html')

    def test_lettings_index_url(self):
        path = reverse('lettings:index')
        assert path == '/lettings/'
        assert resolve(path).view_name == 'lettings:index'

    def test_letting_detail_view(self):
        letting = Letting.objects.all().first()
        path = reverse('lettings:letting', kwargs={'letting_id': letting.id})
        response = self.client.get(path)
        content = response.content.decode()
        assert response.status_code == 200
        assert letting.title in content
        assertTemplateUsed(response, 'lettings/letting.html')

    def test_lettings_detail_url(self):
        letting = Letting.objects.all().first()
        path = reverse('lettings:letting', kwargs={'letting_id': letting.id})
        assert path == '/lettings/' + str(letting.id) + '/'
        assert resolve(path).view_name == 'lettings:letting'
