from django.shortcuts import render
from django.views.generic import ListView
from django.utils import timezone
from backend.models import Contact, Summary, Skill, Service, Fact, Project, Testimony, Education, Experience

class HomeView(ListView):
    model = Testimony
    template_name = 'home.html'
    context_object_name = 'testimonies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['educations'] = Education.objects.all()
        context['experiences'] = Experience.objects.all()

        summary = Summary.objects.get()
        for exp in context['experiences']:
            exp.items = exp.description.split(',')

        context['projects'] = Project.objects.all()
        context['contacts'] = Contact.objects.get()
        context['facts'] = Fact.objects.all()
        context['skills'] = Skill.objects.all()
        context['services'] = Service.objects.all()
        context['dat'] = timezone.now().date()
        context['summar'] = summary

        return context
