from django.contrib import admin
from .models import PortfolioProfile, Skill, Project, Testimonial, ContactMessage

admin.site.register(PortfolioProfile)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Testimonial)
admin.site.register(ContactMessage)
