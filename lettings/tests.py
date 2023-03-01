from django.test import Client, TestCase
from django.urls import reverse
from lettings.models import Letting, Address
from pytest_django.asserts import assertTemplateUsed
import pytest


class TestLettingApp(TestCase):
    client = Client()

    @pytest.mark.django_db
    def setUp(self):
        address = Address.objects.create(
            number=99,
            street='Avenue des Champs-Élysées',
            city='Paris',
            state='Paris',
            zip_code=75008,
            country_iso_code='FRA'
        )
        Letting.objects.create(
            title='Fouquets',
            address=address
        )

    @pytest.mark.django_db
    def test_lettings_index_view(self):
        path = reverse('lettings:index')
        response = self.client.get(path)
        content = response.content.decode()
        assert response.status_code == 200
        assert Letting.objects.all().first().title in content
        assertTemplateUsed(response, 'lettings/index.html')

    @pytest.mark.django_db
    def test_letting_detail_view(self):
        letting = Letting.objects.all().first()
        path = reverse('lettings:letting', kwargs={'letting_id': letting.id})
        response = self.client.get(path)
        content = response.content.decode()
        assert response.status_code == 200
        assert letting.title in content
        assertTemplateUsed(response, 'lettings/letting.html')
