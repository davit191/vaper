from django.db import models
from django.db.models.enums import Choices


# Create your models here.
class category(models.Model):
    title = models.CharField('Վերնագիր', max_length=50)
    slug = models.SlugField('URI', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'կատեգորիա'
        verbose_name_plural = 'Կատեգորիաներ'

class news(models.Model):
    title = models.CharField("վերնագիր", max_length=20)
    text = models.TextField("տեքստ")
    image = models.ImageField("նկար",upload_to = "news")



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "նյութ"
        verbose_name_plural = "նյութեր"

Choicese = [
    ("Instagram", "Instagram"),
    ("Facebook", "Facebook"),
    ("VKontakte", "VKontakte"),
    ("LinkedIn", "LinkedIn"),
    ("Odnoklassniki", "Odnoklassniki"),
]


class social(models.Model):
    
    url = models.URLField("հասցե")
    name = models.CharField('անուն',max_length=15,choices=Choicese)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "կաիք"
        verbose_name_plural = "կաիքեր"

class slide(models.Model):
    image = models.ImageField("նկար",upload_to="slide")
    url = models.URLField("հասցե")
    
    
    def __str__(self):
        return self.url

    class Meta:
        verbose_name = "սլաիդ"
        verbose_name_plural = "սլաիդեր"
    
class personal(models.Model):
    profile = models.CharField('պաշտոն',max_length=100)
    name = models.CharField('անուն', max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "հաստիք"
        verbose_name_plural = "Հաստիքացուցակ"

Cloices = [
    ("Phone","Phone"),
    ("Mail","Mail")
]


class data_contact(models.Model):
    phone = models.CharField("մուտքագրել տվյալ",max_length=30)
    name = models.CharField("տվյալների տեսակ", max_length=20,choices=Cloices)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "հեռախոսահամար"
        verbose_name_plural = "կոնտակտաին տվյալներ"
    
Page_Choice = [
    ("0", "Օգտակար հղումներ"),
    ("1", "Գնորդներին"),
]

class pages(models.Model):
    title = models.CharField("Վերնագիր", max_length=50)
    state = models.CharField('Ում համար', max_length=2, choices=Page_Choice)
    text = models.TextField("տեքստ")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Էջ"
        verbose_name_plural = "Էջեր"