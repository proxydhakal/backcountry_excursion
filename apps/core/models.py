from django.db import models
from solo.models import SingletonModel
from django.utils.html import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    link = models.URLField(null=False)
    cover_image = models.ImageField(upload_to = 'media/slider', null= False)
    

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.cover_image.url))


class Feature(models.Model):
    title = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to ='media/feature', null = False)


    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.image.url))

class Service(models.Model):
    title = models.CharField(max_length=100, null = False)
    description = models.TextField()
    icon_image = models.ImageField(upload_to ='media/service', null=True)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    traveler_name = models.CharField(max_length=255, null=False)
    review_text = models.TextField()
    image_traveler = models.ImageField(upload_to= 'media/testimonial', null=False)

    def __str__(self):
        return self.traveler_name
    



class About(SingletonModel):
    about_comapny = RichTextUploadingField()
    company_image= models.ImageField(upload_to='media/about',null=False)
    class Meta:
        verbose_name = "About Company"

class OurTeam(models.Model):
    name = models.CharField(max_length=100, null= False)
    profile_picture = models.ImageField(upload_to = 'media/team', null= False)
    bio = models.TextField()
    facebook = models.URLField(null=True)
    twitter = models.URLField(null= True)
    instagram = models.URLField(null = True)

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" />' % (self.profile_picture.url))   

class Newsletter(models.Model):
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.email

class Contact(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    message = models.TextField()
    subject = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.subject