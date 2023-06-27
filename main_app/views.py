from django.urls import reverse
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Corgi



# Create your views here.
# Home class is child of TemplateView
# 
class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class CorgisList(TemplateView):
    template_name = "corgis_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # SELECT all 
        #  self.request = dictionary like req.query
        # print(self.request.GET)
        name = self.request.GET.get('name')
        if name != None:
            context["corgis"] = Corgi.objects.filter(name__icontains=name)

        else:
            context["corgis"] = Corgi.objects.all()
        return context

class CorgiCreate(CreateView):
    model = Corgi
    fields = ['name', 'mixes', 'image', 'bio']
    template_name = 'corgi_create.html'
    # what is that?? redirect 
    def get_success_url(self):
        return reverse('corgi_detail', kwargs={'pk':self.object.pk})

class CorgiDetail(DetailView):
    model = Corgi
    template_name = "corgi_detail.html"

class CorgiUpdate(UpdateView):
    model = Corgi
    fields = ['name', 'mixes', 'image', 'bio']
    template_name = "corgi_update.html"
    # success_url = '/corgis/'
    def get_success_url(self):
        return reverse('corgi_detail', kwargs={'pk':self.object.pk})

class CorgiDelete(DeleteView):
    model = Corgi
    template_name = "corgi_delete_confirmation.html"
    success_url = "/corgis/"

