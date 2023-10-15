from django.shortcuts import render
from datetime import datetime
from backend.models import Contact, Skill,Service,Fact

def sidebar(request):
    contacts = Contact.objects.get()
    facts = Fact.objects.all()
    skills = Skill.objects.all()
    services = Service.objects.all()
    date=datetime.now().date 
    return  {'contacts': contacts,'dat': date,'facts': facts,'skills':skills,'services':services}
