from django.db import models

class Contact(models.Model):
    slug = models.SlugField(primary_key=True, unique=True)
    firstname = models.CharField(max_length=255, null=False, blank=False)
    lastname = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    class Meta:
        ordering = ["firstname"]
