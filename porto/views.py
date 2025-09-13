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


from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Contenu de l’email
        subject = f"Nouveau message de {name}"
        body = f"Nom: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject,
                body,
                email,  # From (celui de l’utilisateur)
                ["tfreddyjeanabessolo@gmail.com"],  # To (ton email perso)
                fail_silently=False,
            )
            messages.success(request, "Votre message a bien été envoyé ✅")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'envoi : {e}")

        return redirect("home")  # évite le resubmit du form

    return render(request, "home.html")