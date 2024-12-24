from django.urls import path
from news import views

urlpatterns = [
    path('<int:id>/', views.detail_news, name='detail_news'),
    path('', views.main),
]