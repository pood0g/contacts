from django.db import models
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from base64 import b64encode, b64decode

class Passwords(models.Model):
    
    class Meta:
        ordering = [
            "site"
        ]

    site = models.CharField(max_length=1024)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=1024)
    note = models.CharField(max_length=4096, blank=True, null=True)

    @classmethod
    def encrypt_data(cls, data):
        pass