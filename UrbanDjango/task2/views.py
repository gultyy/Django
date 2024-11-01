from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def welcome(request):
    return render(request, 'second_task/welcome.html')

def func_instance(request):
    return render(request, 'second_task/func_template.html')

class ClassInstance(TemplateView):
    template_name = 'second_task/class_template.html'