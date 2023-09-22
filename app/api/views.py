import requests

from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .models import Address, Contacts, Locale, Libraries
from .serializers import LibrariesSerializer


def parser(request):
    url = 'https://opendata.mkrf.ru/v2/libraries/$'
    headers = {'content-type': 'application/json',
               'X-API-KEY': 'ba73521d9c5049baed810349f63239baf6f4562244229965a408a5b9021b6a33'}
    r = requests.get(url, headers=headers)
    data = r.json()['data']
    for i in data:
        lib = i['data']['general']
        if not Libraries.objects.filter(name=lib['name']):
            address = Address.objects.create(
                street=lib['address']['street'],
                fullAddress=lib['address']['fullAddress']
            )
            try:
                contacts = Contacts.objects.create(phones=lib['contacts']['phones'][0]['value'])
            except IndexError:
                contacts = Contacts.objects.create(phones='None')
            try:
                contacts.website = lib['contacts']['website']
                contacts.save()
            except KeyError:
                pass
            try:
                loc = Locale.objects.get(
                    name=lib['locale']['name'],
                    timezone=lib['locale']['timezone']
                )
            except Locale.DoesNotExist:
                loc = Locale.objects.create(
                    name=lib['locale']['name'],
                    timezone=lib['locale']['timezone']
                )
            library = Libraries.objects.create(
                name=lib['name'],
                description=lib['description'],
                address=address,
                contacts=contacts,
                image=lib['image']['url'],
                locale=loc
            )
    return HttpResponse('OK')


class LibrariesViewSet(viewsets.ModelViewSet):
    queryset = Libraries.objects.all()
    serializer_class = LibrariesSerializer
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'name',
        'description',
        'address__fullAddress',
        'contacts__phones',
        'contacts__website',
        'locale__name',
    ]
    filterset_fields = {
        'name': ['icontains', ],
        'description': ['icontains', ],
        'address__fullAddress': ['icontains', ],
        'contacts__phones': ['icontains', ],
        'contacts__website': ['icontains', ],
        'locale__name': ['icontains', ],
    }