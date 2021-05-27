from django.urls import path

from hierarchy.views import HierarchyView


urlpatterns = [
    path('', HierarchyView.as_view()),
] 
