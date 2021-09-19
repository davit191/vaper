from django.contrib import admin
from django.utils import text
from . import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'return_text', 'return_img']
    list_display_links = ['title', 'return_text', 'return_img']
    readonly_fields = ["return_img"]
    save_on_top = True
    save_as = True

    def return_img(self, obj=None):
        return mark_safe(f"<img style='width:100px;' src='{obj.image.url}'></img>")
    return_img.short_description = "նկար"

    def return_text(self, obj=None):
        return obj.text[:20] + "..." if len(obj.text) > 20 else ""
    return_text.short_description = "տեքստ"


class SlideAdmin(admin.ModelAdmin):
    list_display = ["url",'return_img']
    list_display_links = ["url","return_img"]
    readonly_fields = ["return_img"]
    save_on_top = True
    save_as = True
    
    def return_img(self, obj=None):
        return mark_safe(f"<img style='width:100px;' src='{obj.image.url}'></img>")
    return_img.short_description = "նկար"
   
   

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title",'slug']
    list_display_links = ["title","slug"]
    readonly_fields = []
    save_on_top = True
    save_as = True
    
    

class SocialAdmin(admin.ModelAdmin):
    list_display = ["url","name"]
    list_display_links = ["url","name"]
    save_on_top = True
    save_as = True



class PersonalAdmin(admin.ModelAdmin):
    list_display = ['name','profile',]
    list_display_links = ['name','profile']
    save_on_top = True
    save_as = True

class Data_contactAdmin(admin.ModelAdmin):
    list_display =["phone","name"]
    list_display_links  = ["phone","name"]
    save_on_top = True
    save_as = True






# Register your models here.
admin.site.register(models.category,CategoryAdmin)
admin.site.register(models.social,SocialAdmin)
admin.site.register(models.news, NewsAdmin)
admin.site.register(models.slide,SlideAdmin)
admin.site.register(models.personal, PersonalAdmin)
admin.site.register(models.data_contact,Data_contactAdmin)


