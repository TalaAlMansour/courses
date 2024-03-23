

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('section-detail/', views.section_detail, name='section-detail'),
    

]
