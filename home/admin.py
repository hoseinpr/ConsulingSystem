from django.contrib import admin
from .models import Person, Moshaver, Courses, Course_has_Moshaver, Courses_has_User

@admin.register(Person)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "gpa", "phone")

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ("Title", "Price")

admin.site.register(Moshaver) 
admin.site.register(Course_has_Moshaver)
admin.site.register(Courses_has_User)

