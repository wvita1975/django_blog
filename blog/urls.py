from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post_detail_view"), # post/<int:pk>= de la app muestra el primary key
]
