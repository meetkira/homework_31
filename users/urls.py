from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users import views

urlpatterns = [
    path('', views.index),
    path('user/', views.UserListView.as_view(), name='users'),
    path("user/<int:pk>/", views.UserDetailView.as_view(), name='user'),
    path("create/", views.UserCreateView.as_view(), name='create_user'),
    path("<int:pk>/update/", views.UserUpdateView.as_view(), name='update_user'),
    path("<int:pk>/delete/", views.UserDeleteView.as_view(), name='delete_user'),
    path("token/", TokenObtainPairView.as_view(), name='token'),
    path("token/refresh/", TokenRefreshView.as_view(), name='refresh_token'),
]
