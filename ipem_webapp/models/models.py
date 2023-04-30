from django.db import models
from django.utils.translation import gettext_lazy as _


class Model(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Layer(models.Model):
    class LayerType(models.TextChoices):
        PRODUCT = "PRODUCT", _("Product")
        VALIDATION = "VALIDATION", _("Validation System")
        PRODUCTION = "PRODUCTION", _("Production System")
        STRATEGY = "STRATEGY", _("Strategy")

    class LayerGeneration(models.TextChoices):
        CURRENT = "CURRENT", _("n")
        PREVIOUS_1 = "PREVIOUS_1", _("n-1")
        PREVIOUS_2 = "PREVIOUS_2", _("n-2")
        PREVIOUS_3 = "PREVIOUS_3", _("n-3")
        FOLLOWING_1 = "FOLLOWING_1", _("n+1")
        FOLLOWING_2 = "FOLLOWING_2", _("n+2")
        FOLLOWING_3 = "FOLLOWING_3", _("n+3")

    type = models.CharField(
        max_length=10, choices=LayerType.choices, default=LayerType.PRODUCT
    )
    generation = models.CharField(
        max_length=11, choices=LayerGeneration.choices, default=LayerGeneration.CURRENT
    )
    model = models.ForeignKey(Model, related_name="layer", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.model.name} - Layer: {self.type} ({self.generation})"


class ProblemSolvingActivity(models.Model):
    class ActivityType(models.TextChoices):
        S = "S", _("Situation Analysis")
        P = "P", _("Problem Containment")
        A = "A", _("Detection of Alternative Solutions")
        L = "L", _("Selection of Solutions")
        T = "T", _("Analysis of Consequences")
        E = "E", _("Deciding and Implementing")
        N = "N", _("Recapitulation and Learning")

    type = models.CharField(
        max_length=1, choices=ActivityType.choices, default=ActivityType.S
    )
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.get_type_display()


class DevelopmentActivity(models.Model):
    name = models.CharField(max_length=100)
    layer = models.ForeignKey(
        Layer, related_name="development_activity", on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )
    s = models.OneToOneField(
        ProblemSolvingActivity,
        null=True,
        blank=True,
        related_name="s",
        on_delete=models.CASCADE,
    )
    p = models.OneToOneField(
        ProblemSolvingActivity,
        null=True,
        blank=True,
        related_name="p",
        on_delete=models.CASCADE,
    )
    a = models.OneToOneField(
        ProblemSolvingActivity,
        null=True,
        blank=True,
        related_name="a",
        on_delete=models.CASCADE,
    )
    l = models.OneToOneField(
        ProblemSolvingActivity,
        null=True,
        blank=True,
        related_name="l",
        on_delete=models.CASCADE,
    )
    t = models.OneToOneField(
        ProblemSolvingActivity,
        null=True,
        blank=True,
        related_name="t",
        on_delete=models.CASCADE,
    )
    e = models.OneToOneField(
        ProblemSolvingActivity,
        null=True,
        blank=True,
        related_name="e",
        on_delete=models.CASCADE,
    )
    n = models.OneToOneField(
        ProblemSolvingActivity,
        null=True,
        blank=True,
        related_name="n",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
