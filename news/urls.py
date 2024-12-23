from django.urls import path
from news import views

urlpatterns = [
    path('<int:id>/', views.detail_news, name='detail_news'),
    path('login/', views.login_profile, name='login'),
    path('', views.main),
]