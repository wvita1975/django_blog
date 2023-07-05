from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post_detail_view"), # post/<int:pk>= de la app muestra el primary key
    path('post/new>', PostCreateView.as_view(), name="post_new"),
    path('post/new>', PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name='post_update'),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name='post_delete'),
    
]
