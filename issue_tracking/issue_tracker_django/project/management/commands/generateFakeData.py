from project.models import Project
from ticket.models import Ticket
from django.contrib.auth.models  import User
import random
from faker import Faker
from django.core.management.base import BaseCommand,CommandError



class Command(BaseCommand):
    help = 'Generating fake data'
    def handle(self,*args,**options):
        faker = Faker()
        for name in ['demoadmin','demomanager','demouser']:
            for i in range(4):
                p = Project(name = 'project#'+str(random.randint(3,20)),description = faker.text()[1:30],submitter=User.objects.get(username=name))
                p.save()
            for i in range(20):
                sts =['Open','Backlog','In Progress','Done']
                t = Ticket(title='ticket#'+str(random.randint(1,35)),description = faker.text()[1:30],submitter=User.objects.get(username=name),project=Project.objects.filter(submitter = User.objects.get(username=name))[random.randint(0,3)],status=sts[random.randint(0,3)])
                t.save()