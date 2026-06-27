from django.contrib import admin
from .models import MemberProfile, Education, Skill, Project

admin.site.register(MemberProfile)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Project)