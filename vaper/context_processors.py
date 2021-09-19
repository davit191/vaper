from mainapp.models import category, social, slide

def GetContextGeneratedData(request):
    context = {}
    context['menu'] = category.objects.all()
    context['socials'] = social.objects.all()
    context['slides'] = slide.objects.all()
      
    
    
    return context