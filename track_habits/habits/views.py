from rest_framework import generics, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from habits.models import Habit
from habits.pagination import HabitPagination
from habits.serializers import HabitSerializer, HabitListSerializer
from users.permissions import IsOwner


class HabitListView(generics.ListAPIView):
    serializer_class = HabitListSerializer
    queryset = Habit.objects.all().order_by('id')
    pagination_class = HabitPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'owner']
    ordering_fields = ['name', 'owner']
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user).order_by('id')


class HabitCreateView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()


class HabitDetailView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if len(Habit.objects.filter(associated_habits=instance)) > 0:
            return Response({'error_message': 'Это связанная привычка,'
                                              ' не могу удалить'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class HabitUpdateView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PublicHabitListView(generics.ListAPIView):
    queryset = Habit.objects.filter(is_public=True).order_by('pk')
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
