from django.contrib import admin

from .models import *

admin.site.register(Teacher)
admin.site.register(PCK)
admin.site.register(Qualification_course)
admin.site.register(Tag)
admin.site.register(Event)
# связующие
admin.site.register(Activity)
admin.site.register(Teachers_in_PCK)
admin.site.register(Qualific_course_for_Teachers)
