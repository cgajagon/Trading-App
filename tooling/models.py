from django.db import models
import datetime
from django.urls import reverse
import os

def get_upload_path(instance, filename):
    return os.path.join(
      "user_%s" % instance.tool_id, filename)

class Tool(models.Model):
    tool_id = models.CharField(max_length=50, blank=False, null=False, unique=True)
    tool_description = models.TextField()
    photo = models.ImageField(upload_to=get_upload_path, blank=True)

    def __str__(self):
        return self.tool_id

    def get_absolute_url(self): 
        return reverse('tooling:detail', args=[str(self.pk)])

class Condition(models.Model):
    LOW = 'L'
    MEDIUM = 'M'
    HIGH = 'H'
    
    RISK = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    tool_audited = models.ForeignKey(Tool, on_delete=models.CASCADE)
    total_life = models.IntegerField(default=0, blank=False, null=False)
    remaining_life = models.IntegerField(blank=False, null=False, default=0)
    tool_risk = models.CharField(max_length=1, choices=RISK, default=MEDIUM)
    date_audited = models.DateField(default=datetime.date.today)

    def __str__(self):
        return '%s %s' % (self.tool_audited, self.date_audited)

class Project(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, unique=True)
    def __str__(self):
        return self.title

class ProjectActivity(models.Model):
    project_related = models.ForeignKey(Project, on_delete=models.CASCADE)
    note = models.CharField(max_length=100, blank=False, null=False, unique=True)
    date_enter = models.DateField(default=datetime.date.today)

    def get_absolute_url(self): 
        return reverse('tooling:project_detail', args=[str(self.project_related.pk)])

