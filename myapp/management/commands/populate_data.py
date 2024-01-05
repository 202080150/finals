from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from faker import Faker
from myapp.models import Category, Pond, Fish, Fisherman, FishingRecord
from datetime import date, datetime

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **kwargs):
        self.populate_categories()
        self.populate_ponds()
        self.populate_fishes()
        self.populate_fishermen()
        self.populate_fishing_records()
        self.stdout.write(self.style.SUCCESS('Dummy data has been successfully populated.'))

    def populate_categories(self):
        categories = ['Freshwater', 'Saltwater', 'Tropical']
        for category_name in categories:
            Category.objects.get_or_create(name=category_name)

    def populate_ponds(self):
        ponds_data = [
            {'name': fake.word(), 'location': fake.word()},
            {'name': fake.word(), 'location': fake.word()},
            {'name': fake.word(), 'location': fake.word()},
        ]
        for pond_data in ponds_data:
            Pond.objects.create(**pond_data)

    def populate_fishes(self):
        categories = Category.objects.all()
        ponds = Pond.objects.all()

        for _ in range(20):
            fish = Fish.objects.create(
                species=fake.word(),
                color=fake.word(),
                size=fake.random_int(1, 50),
                category=fake.random_element(categories),
            )
            fish.ponds.set(fake.random_elements(ponds, length=fake.random_int(1, 3)))


    def populate_fishermen(self):
        fishes = Fish.objects.all()
        for _ in range(5):
            Fisherman.objects.create(
                name=fake.name(),
                email=fake.email(),
                favorite_fish=fake.random_element(fishes),
            )

    def populate_fishing_records(self):
        fishes = Fish.objects.all()
        fishermen = Fisherman.objects.all()
        for _ in range(10):
            FishingRecord.objects.create(
                date=fake.date_this_decade(),
                time=fake.date_time_this_decade(),
                fish=fake.random_element(fishes),
                fisherman=fake.random_element(fishermen),
            )
