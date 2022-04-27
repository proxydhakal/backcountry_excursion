from django.contrib import admin
from apps.core.models import Slider, Feature, Service, Testimonial, About, OurTeam, Contact, Newsletter
from solo.admin import SingletonModelAdmin
# Register your models here.

class SliderAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')

admin.site.register(Slider, SliderAdmin)

class FeatureAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')

admin.site.register(Feature, FeatureAdmin)
admin.site.register(About, SingletonModelAdmin)
admin.site.register(Service)
admin.site.register(Testimonial)

class OurTeamAdmin(admin.ModelAdmin):
    list_display =('name', 'image_tag')

admin.site.register(OurTeam, OurTeamAdmin)
admin.site.register(Newsletter)

class ContactAdmin(admin.ModelAdmin):
    list_display=('f_name', 'l_name', 'email','subject','message')
    def changelist_view(self, request, extra_context=None):
        self.list_display_links = (None, )
        return super(ContactAdmin, self).changelist_view(request, extra_context=None)
admin.site.register(Contact,ContactAdmin)