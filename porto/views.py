from django.shortcuts import render, redirect
from .models import Project
from django.shortcuts import render, get_object_or_404
from .models import PortfolioProfile, Skill, Project, Testimonial, ContactMessage

def home(request):
    profile = PortfolioProfile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    testimonials = Testimonial.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            return redirect("home")

    context = {
        "profile": profile,
        "skills": skills,
        "projects": projects,
        "testimonials": testimonials,
    }
    return render(request, "home.html", context)

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "project_detail.html", {"project": project})
