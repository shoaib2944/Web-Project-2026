from django.db import models
from bio.models import MemberProfile

class Skill(models.Model):
    member = models.ForeignKey(MemberProfile, on_delete=models.CASCADE, related_name='skills')
    category = models.CharField(max_length=100)
    skills_list = models.TextField()

    def __str__(self):
        return f"{self.category} for {self.member.name}"