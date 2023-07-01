from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post_detail_view"), # post/<int:pk>= de la app muestra el primary key
    path('post/new>', PostCreateView.as_view(), name="post_new")
]
