from django.db import models
from bio.models import MemberProfile

class Education(models.Model):
    member = models.ForeignKey(MemberProfile, on_delete=models.CASCADE, related_name='education_history')
    degree_title = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    duration_or_grad_year = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.degree_title} - {self.member.name}"