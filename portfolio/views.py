from django.shortcuts import render
from .models import Category, Project, Skill, Experience

def index(request):
    categories = Category.objects.all().prefetch_related('projects')
    skills = Skill.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')
    
    # Group skills by category for better display
    skills_by_cat = {}
    for skill in skills:
        if skill.category not in skills_by_cat:
            skills_by_cat[skill.category] = []
        skills_by_cat[skill.category].append(skill)
    
    context = {
        'categories': categories,
        'skills_by_cat': skills_by_cat,
        'experiences': experiences,
    }
    return render(request, 'portfolio/index.html', context)
