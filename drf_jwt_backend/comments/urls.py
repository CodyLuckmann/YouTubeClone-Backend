from django.urls import path
from comments import views
urlpatterns = [
    path('comments/<str:video_id>/', views.get_comments_by_Id),
    path('', views.user_comments),
    path('reply/', views.reply_to_comments),
    path('replies/<int:comment_id>/', views.get_replies),
    path('update/<int:comment_id>', views.update_comment),
    path('delete/<int:comment_id>', views.delete_comment)
]