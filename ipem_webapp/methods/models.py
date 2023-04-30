from django.db import models


class Method(models.Model):
    name = models.CharField(max_length=100)
    alternative_name = models.CharField(max_length=200, null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
