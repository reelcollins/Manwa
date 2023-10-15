# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Contact, Skill, Service, Fact, Project, Testimony, Summary, Education, Experience, Contactme,ProjectImage
from .forms import ContactForm, SkillForm, ServiceForm, FactForm, ProjectForm, TestimonyForm, SummaryForm, EducationForm, ExperienceForm

class DashboardView(ListView):
    model = Service
    template_name = 'dashboard.html'
    context_object_name = 'services'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skillscount'] = Skill.objects.count()
        context['projectscount'] = Project.objects.count()
        return context

class PersonalInformationView(DetailView):
    model = Contact
    template_name = 'personal-information.html'
    context_object_name = 'contacts'

class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_form.html'

    def get_success_url(self):
        return reverse('contact_update', kwargs={'pk': self.object.pk})

class SkillListView(ListView):
    model = Skill
    template_name = 'skills.html'
    context_object_name = 'skills'

class SkillDetailView(DetailView):
    model = Skill
    template_name = 'skill_detail.html'
    context_object_name = 'skill'

class SkillCreateView(CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skill_form.html'
    success_url = reverse_lazy('skill_list')

class SkillUpdateView(UpdateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skill_form.html'
    success_url = reverse_lazy('skill_list')

class SkillDeleteView(DeleteView):
    model = Skill
    template_name = 'skill_confirm_delete.html'
    success_url = reverse_lazy('skill_list')
class ServiceListView(ListView):
    model = Service
    template_name = 'services.html'
    context_object_name = 'services'
class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_detail.html'
    context_object_name = 'service'
class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service_form.html'
    success_url = '/service_list/'  
class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service_form.html'
    success_url = '/service_list/'  
class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'service_confirm_delete.html'
    success_url = '/service_list/'  


class ContactFormSubmitView(CreateView):
    model = Contactme
    fields = ['name', 'email', 'subject', 'message']
    template_name = 'contact_form_submit.html'
    success_url = reverse_lazy('home')

class MessagesListView(ListView):
    model = Contactme
    template_name = 'messages.html'
    context_object_name = 'messages'
class FactListView(ListView):
    model = Fact
    template_name = 'facts.html'
    context_object_name = 'facts'

class FactDetailView(DetailView):
    model = Fact
    template_name = 'fact_detail.html'
    context_object_name = 'fact'

class FactCreateView(CreateView):
    model = Fact
    form_class = FactForm
    template_name = 'fact_form.html'
    success_url = '/fact_list/'  

class FactUpdateView(UpdateView):
    model = Fact
    form_class = FactForm
    template_name = 'fact_form.html'
    success_url = '/fact_list/'  

class FactDeleteView(DeleteView):
    model = Fact
    template_name = 'fact_confirm_delete.html'
    success_url = '/fact_list/'  

class ProjectListView(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio-details.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()  # Get the Project object
        context['images'] = project.images.all()
        return context

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'project_form.html'
    form_class = ProjectForm
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        # Save the main project details
        response = super().form_valid(form)

        # Save additional images
        images = self.request.FILES.getlist('images')
        for image in images:
            ProjectImage.objects.create(project=self.object, image=image)

        return response 

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_form.html'
    success_url = '/project_list/'  

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = '/project_list/'  

# Testimony Views
class TestimonyListView(ListView):
    model = Testimony
    template_name = 'testimonies.html'
    context_object_name = 'testimonies'

class TestimonyDetailView(DetailView):
    model = Testimony
    template_name = 'portfolio-details.html'
    context_object_name = 'testimony'

class TestimonyCreateView(CreateView):
    model = Testimony
    form_class = TestimonyForm
    template_name = 'testimony_form.html'
    success_url = '/testimony_list/'  

class TestimonyUpdateView(UpdateView):
    model = Testimony
    form_class = TestimonyForm
    template_name = 'testimony_form.html'
    success_url = '/testimony_list/'  

class TestimonyDeleteView(DeleteView):
    model = Testimony
    template_name = 'testimony_confirm_delete.html'
    success_url = '/testimony_list/'  


# Summary View
class SummaryUpdateView(UpdateView):
    model = Summary
    form_class = SummaryForm
    template_name = 'summary_form.html'

    def get_success_url(self):
        return reverse('summary_update', kwargs={'pk': 1})


# Education Views
class EducationListView(ListView):
    model = Education
    template_name = 'education.html'
    context_object_name = 'educations'

class EducationDetailView(DetailView):
    model = Education
    template_name = 'portfolio-details.html'
    context_object_name = 'education'

class EducationCreateView(CreateView):
    model = Education
    form_class = EducationForm
    template_name = 'education_form.html'
    success_url = '/education_list/'  

class EducationUpdateView(UpdateView):
    model = Education
    form_class = EducationForm
    template_name = 'education_form.html'
    success_url = '/education_list/'  

class EducationDeleteView(DeleteView):
    model = Education
    template_name = 'education_confirm_delete.html'
    success_url = '/education_list/'  


# Experience Views
class ExperienceListView(ListView):
    model = Experience
    template_name = 'experience.html'
    context_object_name = 'experiences'

class ExperienceDetailView(DetailView):
    model = Experience
    template_name = 'portfolio-details.html'
    context_object_name = 'experience'

class ExperienceCreateView(CreateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'experience_form.html'
    success_url = '/experience_list/'  

class ExperienceUpdateView(UpdateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'experience_form.html'
    success_url = '/experience_list/'  

class ExperienceDeleteView(DeleteView):
    model = Experience
    template_name = 'experience_confirm_delete.html'
    success_url = '/experience_list/'  


def contact_form_submit(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Perform any additional validation here if required

        # Save the form data to the database
        submission = Contactme.objects.create(name=name, email=email, subject=subject, message=message)

        # Optionally, you can add logic to send an email notification or perform other actions here.

        return redirect('home')
    else:
          return redirect('home')

def messages_list(request):
    message = Contactme.objects.all()
    return render(request, 'messages.html', {'messages': message})