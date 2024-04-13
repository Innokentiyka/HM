from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.apps import UsersConfig
from users.views import (UserCreateAPIView, UserUpdateAPIView,
                         UserDestroyAPIView, UserRetrieveAPIView,
                         UserListAPIView, MyTokenObtainPairView)


app_name = UsersConfig.name

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('create/', UserCreateAPIView.as_view(), name='user_create'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(),
         name='user_delete'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(),
         name='user_update'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('list/', UserListAPIView.as_view(), name='user_list'),
]
