from project.models import Project
from faker import Faker
from django.core.management.base import BaseCommand,CommandError



class Command(BaseCommand):
    help = 'Generating fake data'
    def handle(self,*args,**options):
        faker = Faker()
        for i in range(4):
            p = Project(name = faker.text()[1:10],description = faker.text()[1:30])
            p.save()