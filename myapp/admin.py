from django.contrib import admin
from .models import Category, Pond, Fish, Fisherman, FishingRecord

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

@admin.register(Pond)
class PondAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'created_at', 'updated_at')

@admin.register(Fish)
class FishAdmin(admin.ModelAdmin):
    list_display = ('species', 'color', 'size', 'category', 'created_at', 'updated_at')
    filter_horizontal = ('ponds',)

@admin.register(Fisherman)
class FishermanAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'favorite_fish', 'created_at', 'updated_at')

@admin.register(FishingRecord)
class FishingRecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'fish', 'fisherman', 'created_at', 'updated_at')
