from django.urls import path
from posts.views import *

app_name = 'posts'
urlpatterns = [
    path('post/create/', PostCreateView.as_view()),
    path('all/', PostsListView.as_view()),
    path('post/detail/<int:pk>/', PostDetailView.as_view()),
]
