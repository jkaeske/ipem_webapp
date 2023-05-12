from django.db import models


class Heading(models.Model):
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.text[:30]

    class Meta:
        verbose_name = "Heading"


class Text(models.Model):
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.text[:30]

    class Meta:
        verbose_name = "Text"


class BulletPoint(models.Model):
    text = models.TextField(null=True, blank=True)

    # StreamField option for list of objects
    as_list = True

    def __str__(self):
        return self.text[:30]

    class Meta:
        verbose_name = "Bullet point"
        verbose_name_plural = "Bullet points"


# Register blocks for StreamField as list of models
STREAMBLOCKS_MODELS = [
    Heading,
    Text,
    BulletPoint,
]
