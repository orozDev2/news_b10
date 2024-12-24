from django.urls import path

from workspace import views

urlpatterns = [
    path('create-news/', views.create_news, name='create_news'),
    path('update-news/<int:id>/', views.update_news, name='update_news'),
    path('delete-news/<int:id>/', views.delete_news, name='delete_news'),
    path('', views.workspace, name='workspace'),
]