from django.urls import path
from .views import (
    PostDetailView,
    BlogView,
    AddPostView,
    UpdatePostView,
    PostsByTagListView,
    PostsByCategoryListView,
    PreviewPostView,
    AddCategoryView,
    AddTagView,
    UpdateCategoryView
)

urlpatterns = [
    path("<slug:slug>/view/", PostDetailView.as_view(), name="post_by_slug"),
    path("", BlogView.as_view(), name="blog"),

    path("add_post/", AddPostView.as_view(), name="add_post"),
    path("update_post/<slug:post_slug>/", UpdatePostView.as_view(), name="update_post"),
    path("add_category/", AddCategoryView.as_view(), name="add_category"),
    path('update_category/<slug:category_slug>/', UpdateCategoryView.as_view(), name='update_category'),
    path("add_tag/", AddTagView.as_view(), name="add_tag"),

    path('tag/<slug:tag>/', PostsByTagListView.as_view(), name='posts_by_tag'),
    path('category/<slug:category>/', PostsByCategoryListView.as_view(), name='posts_by_category'),
    path('preview/', PreviewPostView.as_view(), name='preview_post'),
]