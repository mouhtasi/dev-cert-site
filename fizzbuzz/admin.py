from django.contrib import admin
from .models import Topic, Lesson, Test
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from fizzbuzz.models import Student


# Define an inline admin descriptor for Student model
class StudentInLine(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'student'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (StudentInLine, )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Topic)
admin.site.register(Lesson)
admin.site.register(Test)
