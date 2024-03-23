
from django.shortcuts import render
from .models import Course,Section,Level,News



def home_page(request):
    
     
    news = News.objects.all()
    
    context = {
       
        'news': news,
    }
    
    return render(request, 'home.html', context)

def section_detail(request, section_slug):
    section = Section.objects.get(section_Slug=section_slug)

    context = {
        'section': section,
        'levels': section.level_set.all()
    }

    return render(request, 'courses.html', context)

