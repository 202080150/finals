from django.db import models
from django.utils.crypto import get_random_string
from faker import Faker
from datetime import date, datetime

fake = Faker()

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Pond(BaseModel):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Fish(BaseModel):
    species = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    size = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='fishes')
    ponds = models.ManyToManyField(Pond, related_name='fishes')

    def __str__(self):
        return self.species

class Fisherman(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    favorite_fish = models.ForeignKey(Fish, on_delete=models.CASCADE, related_name='fans')

    def __str__(self):
        return self.name

class FishingRecord(BaseModel):
    date = models.DateField()
    time = models.DateTimeField()
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE, related_name='fishing_records')
    fisherman = models.ForeignKey(Fisherman, on_delete=models.CASCADE, related_name='fishing_records')

    def __str__(self):
        return f"{self.fisherman.name} caught {self.fish.species} on {self.date} at {self.time}"
