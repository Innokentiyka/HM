from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitListView, HabitCreateView, HabitDetailView,
                          HabitUpdateView, HabitDestroyView,
                          PublicHabitListView)


app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitListView.as_view(), name='habits_list'),
    path('public/', PublicHabitListView.as_view(), name="habits_public_list"),
    path('create/', HabitCreateView.as_view(), name='habits_create'),
    path('<int:pk>', HabitDetailView.as_view(), name='habits_detail'),
    path('update/<int:pk>/', HabitUpdateView.as_view(),
         name='habits_update'),
    path('delete/<int:pk>/', HabitDestroyView.as_view(),
         name='habits_delete'),
]
