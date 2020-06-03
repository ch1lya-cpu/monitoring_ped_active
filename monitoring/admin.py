from django.contrib import admin


from .models import Role, Qualification, Teacher, Event, Qualific_course, Category, Achievement, Type_educ, \
    Staging_on_teacher, Teachers_has_qualific_course, Teachers_has_type_educ, Achievements_has_teachers, \
    Teachers_has_event


admin.site.register(Role)
admin.site.register(Qualification)
admin.site.register(Teacher)
admin.site.register(Event)
admin.site.register(Qualific_course)
admin.site.register(Category)
admin.site.register(Achievement)
admin.site.register(Type_educ)
admin.site.register(Staging_on_teacher)
admin.site.register(Teachers_has_qualific_course)
admin.site.register(Teachers_has_type_educ)
admin.site.register(Achievements_has_teachers)
admin.site.register(Teachers_has_event)