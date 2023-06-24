from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Corgis



# Create your views here.
# Home class is child of TemplateView
# 
class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

# class Corgis:
#     def __init__(self, name, mixes, image, bio):
#         self.name = name
#         self.mixes = mixes
#         self.image = image
#         self.bio = bio

# corgis = [
#     Corgis("Corgsky", "Husky X Corgi",
#     "https://www.101dogbreeds.com/wp-content/uploads/2018/07/Corgsky.jpg",
#     "It is friendly, loyal, and gentle, inheriting the fun-loving nature of both its parents, which makes it a great family pet well-suited for all ages." ),
#     Corgis("Corman Shepherd", "German Shepherd X Corgi", 
#     "https://www.101dogbreeds.com/wp-content/uploads/2016/11/Corman-Shepherd.jpg",
#     "Intelligent, smart, and easy to please, they replicate their German Shepherd parent when it comes to being loyal, protective, and dedicated."),
#     Corgis("Beagi", "Beagle X Corgi", 
#     "https://www.101dogbreeds.com/wp-content/uploads/2015/09/Beagi.jpg",
#     "The drooping ears of the Beagle and the striped appearance of the Corgi (on the eyes and nose) make these amicable, intelligent, and loyal dogs immensely adorable. Most of them even display the strong smelling and hunting instincts of both their parents.")
# ]

class CorgisList(TemplateView):
    template_name = "corgis_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # SELECT all 
        #  self.request = dictionary like req.query
        # print(self.request.GET)
        name = self.request.GET.get('name')
        if name != None:
            context["corgis"] = Corgis.objects.filter(name__icontains=name)

        else:
            context["corgis"] = Corgis.objects.all()
        return context

