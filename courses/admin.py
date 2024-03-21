from django.contrib import admin
from .models import Course, Section, Level, News


# =============== Course Model =================
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('coursename', 'created_at', 'update_at')
    search_fields = ('coursename',)
    list_filter = ('created_at', 'update_at')


admin.site.register(Section)

admin.site.register(Level)

admin.site.register(News)
