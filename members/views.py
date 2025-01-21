from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


# def members(request):
#     return HttpResponse("Hello world!")
# def members(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, slug):
  mymember = Member.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'fruits': ['Apple', 'Banana', 'Cherry'],   
#   }
#   return HttpResponse(template.render(context, request))

# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'firstname': 'Linus',
#   }
#   return HttpResponse(template.render(context, request))    
# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'cars': [
#       {
#         'brand': 'Ford',    ИСПРАВИТЬ
#         'model': 'Mustang',
#         'year': '1964',
#       },
#       {
#         'brand': 'Ford',
#         'model': 'Bronco',
#         'year': '1970',
#       },
#       {
#         'brand': 'Volvo',
#         'model': 'P1800',
#         'year': '1964',
#       }]
#     }
#   return HttpResponse(template.render(context, request)) 

def testing(request):
  template = loader.get_template('template.html')
  return HttpResponse(template.render())          

# def testing(request):
#   mymembers = Member.objects.all().values()
#   template = loader.get_template('template.html')
#   context = {
#     'mymembers': mymembers,
#   }
#   return HttpResponse(template.render(context, request))       