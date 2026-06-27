from django.db import models


class MemberProfile(models.Model):
    # Bio Section
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text="e.g., shoaib or shaheryar")
    job_title = models.CharField(max_length=100, default="BSCS Student")
    professional_description = models.TextField()

    def __str__(self):
        return self.name


class Education(models.Model):
    member = models.ForeignKey(MemberProfile, on_delete=models.CASCADE, related_name='education_history')
    degree_title = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    duration_or_grad_year = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.degree_title} - {self.member.name}"


class Skill(models.Model):
    member = models.ForeignKey(MemberProfile, on_delete=models.CASCADE, related_name='skills')
    category = models.CharField(max_length=100, help_text="e.g., Languages, Tools, Soft Skills")
    skills_list = models.TextField(help_text="Separate with commas")

    def __str__(self):
        return f"{self.category} for {self.member.name}"


class Project(models.Model):
    member = models.ForeignKey(MemberProfile, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.member.name}"