from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('post/', views.PostListView.as_view(), name='post-list'),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete')
]