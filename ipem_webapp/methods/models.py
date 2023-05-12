from django.core.validators import MaxValueValidator
from django.db import models

from ipem_webapp.models.models import DevelopmentActivity


class Method(models.Model):
    name = models.CharField(max_length=100)
    alternative_name = models.CharField(max_length=200, null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    s_rating = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(5)]
    )
    p_rating = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(5)]
    )
    a_rating = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(5)]
    )
    l_rating = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(5)]
    )
    t_rating = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(5)]
    )
    e_rating = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(5)]
    )
    n_rating = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(5)]
    )
    activity = models.ManyToManyField(
        DevelopmentActivity, related_name="method", through="MethodRegistry"
    )

    def __str__(self):
        return self.name


class MethodRegistry(models.Model):
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    development_activity = models.ForeignKey(
        DevelopmentActivity, on_delete=models.CASCADE
    )
    rating = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(5)]
    )
