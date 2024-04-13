from django.contrib import admin
from habits.models import Habit


@admin.register(Habit)
class HabitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'place', 'time', 'action',
                    'is_pleasure', 'associated_habits', 'periodic',
                    'award', 'time_exec', 'is_public')
    list_filter = ('name', 'owner', 'place')
