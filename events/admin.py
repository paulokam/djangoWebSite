from importlib.util import module_for_loader
from django.contrib import admin

from .models import Category, Event

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","id"]

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "category",
        "year",
        "month",
        "description",
        "image",
    ]