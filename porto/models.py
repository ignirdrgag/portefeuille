from django.db import models
from django.utils.text import slugify

# Profil
class PortfolioProfile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    bio = models.TextField()
    photo = models.ImageField(upload_to="profile/", default="profile/default.png")
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    # Nouveaux champs
    age = models.PositiveIntegerField(blank=True, null=True)
    degree = models.CharField(max_length=150, blank=True, null=True, help_text="Ex: Licence, Master, Doctorat")

    def __str__(self):
        return self.name


# Compétences
class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50, help_text="Classe FontAwesome ex: fa-code")

    def __str__(self):
        return self.name


# Projets
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    long_description = models.TextField(blank=True, null=True)  # description plus complète
    technologies = models.CharField(max_length=255, blank=True, null=True)  # ex: Django, React, Tailwind
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    #     for p in Project.objects.all():
    #         if not p.slug:
    #             p.slug = slugify(p.title)
    #             p.save()


# Témoignages
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    photo = models.ImageField(upload_to="testimonials/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.role}"


# Messages de contact
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.name}"
