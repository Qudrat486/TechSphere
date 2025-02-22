from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="home"),
    
    path("post/<int:id>/<slug:slug>/", views.article_detail_view, name="post_detail"),
    path("create-post/", views.create_post_view, name="create-post"),
    path("create-comment/<int:post_id>/", views.add_comment_to_post_view, name="create-comment"),
    path(
        "delete-comment/<int:comment_id>/",
        views.delete_comment_view,
        name="delete-comment",
    ),
    path("update-comment/<int:comment_id>/", views.update_comment, name="update-comment"),
]
