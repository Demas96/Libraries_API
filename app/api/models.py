from django.db import models


class Address(models.Model):
    street = models.TextField(blank=True)
    fullAddress = models.TextField(blank=True)

    def __str__(self):
        return self.street


class Contacts(models.Model):
    website = models.TextField(blank=True)
    phones = models.TextField(blank=True)

    def __str__(self):
        return f'{self.website} {self.phones}'


class Locale(models.Model):
    name = models.TextField(blank=True, unique=True)
    timezone = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Libraries(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    address = models.ForeignKey('Address', on_delete=models.PROTECT, null=True)
    contacts = models.ForeignKey('Contacts', on_delete=models.PROTECT, null=True)
    image = models.TextField(blank=True)
    locale = models.ForeignKey('Locale', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

