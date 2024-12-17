from django.urls import path
from news import views

urlpatterns = [
    path('', views.main),
    path('<int:id>/', views.detail_news, name='detail_news'),
]