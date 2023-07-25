from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


# Speakers model

class Speaker(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, unique=True)
    bio = models.TextField(max_length=200, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='media/profile_pictures', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Speakers'

    def __str__(self):
        return self.name
