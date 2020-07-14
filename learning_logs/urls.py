"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics
    path('topics/', views.topics, name='topics'),
    # Detail page for a single Page
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
