from mainapp.models import category, social, slide, pages, data_contact


def GetContextGeneratedData(request):
    context = {}
    context["menu"] = category.objects.all()
    context["socials"] = social.objects.all()
    context["slides"] = slide.objects.all()
    context["useful"] = pages.objects.filter(state="0")
    context["foruser"] = pages.objects.filter(state="1")
    # context['first_number'] = data_contact.objects.filter(name="Phone").first()
    context["data_contact"] = data_contact.objects.all().order_by("-name")

    return context
