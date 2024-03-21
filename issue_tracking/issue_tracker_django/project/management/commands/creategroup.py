from django.contrib.auth.models  import Group,User, Permission
from django.core.management.base import BaseCommand,CommandError
from django.contrib.contenttypes.models import ContentType
from project.models import Project
from ticket.models import Ticket


class Command(BaseCommand):
    help = 'Creating groups'
    def handle(self, *args,**options):
        try:
            admin_group,created = Group.objects.get_or_create(name='admin') 
            manager_group,created = Group.objects.get_or_create(name='manager') 
            cuser_group,created = Group.objects.get_or_create(name='cuser')
        except:
            raise CommandError('Something was not able to create group or group doesnt exist')
        # u = User.objects.all()
        # for uu in u:
        #     cuser_group.user_set.add(uu)
        #     if uu.username!='admin' and uu.username!='Aisultan':
        #         uu.delete()
    

        ct = ContentType.objects.get_for_model(Project)
        ct_ticket = ContentType.objects.get_for_model(Ticket)
        project_permission = Permission.objects.filter(content_type = ct)
        ticket_permission =Permission.objects.filter(content_type=ct_ticket)

        for p in project_permission:
            if p.codename == 'delete_project':
                admin_group.permissions.add(p)

            elif p.codename == 'change_project':
                admin_group.permissions.add(p)
                manager_group.permissions.add(p)
            elif p.codename =='add_project':
                admin_group.permissions.add(p)
                manager_group.permissions.add(p)
            else:
                cuser_group.permissions.add(p)
                admin_group.permissions.add(p)
                manager_group.permissions.add(p)
        u  = User.objects.get(username = 'Aisultan')
        print(u.has_perm('project.add_project'))