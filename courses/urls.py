""" from .import views
from django.urls import include,path
urlpatterns = [

   path('', views.course_list, name='course_list'),
]  """


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('section-detail/', views.section_detail, name='section-detail'),

]
