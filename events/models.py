from django.db import models

class Event(models.Model):

    class Meta:
        ordering = ['event_start']

    COLOUR_CHOICES = {
        ("RED", "#FF0000"),
        ("GRN", "#00FF00"),
        ("BLU", "#0000FF"),
    }

    slug = models.SlugField(primary_key=True, unique=True, max_length=16)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=250)
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()
    all_day = models.BooleanField(default=False)
    background_color = models.CharField(choices=COLOUR_CHOICES, max_length=3)
