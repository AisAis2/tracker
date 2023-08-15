from django.db import models
from project.models import Project
from django.contrib.auth.models import User

class Ticket(models.Model):
    description = models.TextField(blank = True, null = True)
    title = models.CharField(max_length=200, null = False)
    submitter = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    assigned = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='assignee', null=True)
    project= models.ForeignKey(Project, on_delete = models.CASCADE, null=True)
    priorities = [
			('Low','Low'),
			('Medium','Medium'),
			('High', 'High'),
    ]
    statuses =[
		('Open','Open'),
    ('Backlog','Backlog'),
		('Done','Done'),
		('In Progress', 'In Progress'),
		]
    tps = [
		('Bugs/errors','Bugs/errors'),
		('Feature Requests','Feature Requests'),
		('Other Comments','Other Comments'),
	]
    priority = models.CharField(
        max_length=20,
        choices=priorities,
        default= 'Low'
    )
    status = models.CharField(
		max_length=20,
		choices = statuses,
		default = 'Open'
	)
    created = models.TimeField("Created", auto_now=False, auto_now_add=True)
    type = models.CharField(
        max_length=30,
        choices = tps,
        default= 'Other Comments'
    )
    class Meta:
        app_label = 'ticket'
    def __str__(self):
      return self.title

