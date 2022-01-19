from django.urls import path
from comments import views

urlpatterns = [
    path('all/', views.get_all_comments),
    
]