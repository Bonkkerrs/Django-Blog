from django.contrib import admin
from course_page.models import Course, CanvasUserAccount
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name','course_code','semester','course_id')
    search_fields = ['course_name','course_code','semester','course_id']
    list_per_page = 15
    list_filter = ('semester',)

class CanvasUserAccountAdmin(admin.ModelAdmin):
    list_display = ('canvas_id', 'name', 'physical_id', 'origin')
    search_fields = ['canvas_id', 'name', 'physical_id','origin__course_name']
    list_per_page = 50

admin.site.register(Course,CourseAdmin)
admin.site.register(CanvasUserAccount,CanvasUserAccountAdmin)