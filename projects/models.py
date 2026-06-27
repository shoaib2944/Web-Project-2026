from django.db import models
from bio.models import MemberProfile

class Project(models.Model):
    member = models.ForeignKey(MemberProfile, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.member.name}"