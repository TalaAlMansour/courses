from django.contrib import admin
from .models import Course, Section, Level, News
from django import forms


class SectionAdminForm(forms.ModelForm):
    class Meta:
        model = Section
        exclude = ['section_Slug']


# =============== Course Model =================
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('coursename', 'created_at', 'update_at')
    search_fields = ('coursename',)
    list_filter = ('created_at', 'update_at')


# =============== Section Model =================
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    form = SectionAdminForm
    list_display = ('sectiontitle', 'course', 'created_at', 'update_at')
    search_fields = ('sectiontitle', 'description',)
    list_filter = ('created_at', 'update_at',)


# =============== Level Model =================
@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    search_fields = ('levelTitle', 'levelDescription',)
    list_filter = ('created_at', 'update_at',)
    list_display = ('levelTitle', 'section', 'created_at', 'update_at',)


# =============== News Model =================
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ('news_title', 'news_desc',)
    list_filter = ('created_at', 'update_at',)
    list_display = ('news_title', 'news_date', 'lessonsNum',
                    'created_at', 'update_at',)
