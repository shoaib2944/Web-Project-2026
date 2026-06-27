from django.db import models

class MemberProfile(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    job_title = models.CharField(max_length=100, default="BSCS Student")
    professional_description = models.TextField()

    def __str__(self):
        return self.name