from django.contrib.auth.models  import Group,User
from django.core.management.base import BaseCommand,CommandError

class Command(BaseCommand):
    help = 'Creating groups'
    def handle(self, *args,**options):
        try:
            admin_group,created = Group.objects.get_or_create(name='admin') 
            manager_group,created = Group.objects.get_or_create(name='manager') 
            cuser_group,created = Group.objects.get_or_create(name='cuser')
        except:
            raise CommandError('Something was not able to create group or group doesnt exist')
        u = User.objects.all()
        for uu in u:
            cuser_group.user_set.add(uu)