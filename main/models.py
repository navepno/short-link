from django.db import models


class Link(models.Model):
    original_link = models.CharField(max_length=256, blank=True)
    short_link = models.URLField()
    # creation_date = models.DateTimeField('creation date')
