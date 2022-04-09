from django.db import models

class Contact(models.Model):
    firstname = models.CharField(max_length=255, null=False, blank=False)
    lastname = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    class Meta:
        ordering = ["firstname"]
