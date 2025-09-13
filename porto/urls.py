from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import contact_view


urlpatterns = [
    path('', views.home, name='home'),
    path("project_detail", views.project_detail, name="project_detail"),
    path("contact/", contact_view, name="contact"),

]
