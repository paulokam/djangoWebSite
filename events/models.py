from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    class Meta:
        ordering = ("id",)
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    
    def __str__(self):
        return self.name


class Event(models.Model):
    category = models.ForeignKey(Category, related_name="events", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    image = models.ImageField(upload_to="events/images", blank=True)
    year = models.IntegerField()
    month = models.IntegerField()
    description = models.TextField(blank=True)
    
    objects = models.Manager()

    class Meta:
        ordering = ("year","month",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("events:detail", kwargs={"slug": self.slug})