from django.urls import path
from . import views

# Note empty string signifies homepage (i.e. /project)
# The name prop allows us to link to the view in the markup, rather than the full url
urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>', views.project, name='project'),
]
