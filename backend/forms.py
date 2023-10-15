from django import forms
from multiupload.fields import MultiFileField
from .models import Contact, Skill, Service, Fact, Project, Testimony, Summary, Education, Experience

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'contact', 'location', 'city', 'website', 'degree', 'dob', 'position', 'facebook', 'linkedin', 'twitter', 'photo', 'about']

class SkillForm(forms.ModelForm):
    experience = forms.IntegerField(
        max_value=100,
        widget=forms.TextInput(attrs={'max': 100})
    )

    class Meta:
        model = Skill
        fields = ['name', 'experience']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'icon', 'description']

class FactForm(forms.ModelForm):
    class Meta:
        model = Fact
        fields = ['title', 'count', 'icon', 'description']

class ProjectForm(forms.ModelForm):
    images = MultiFileField(
        min_num=1,
        max_num=10,
        max_file_size=1024*1024*5,  # 5MB limit per file
        required=False
    )

    class Meta:
        model = Project
        fields = ['project', 'category', 'client', 'technologies', 'url', 'project_date', 'url', 'image', 'description']
class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['client', 'company', 'message']

class SummaryForm(forms.ModelForm):
    class Meta:
        model = Summary
        fields = ['message']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['acquirement', 'institution', 'timeline']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'company', 'timeline', 'description']
