from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from habits.models import Habit
from habits.validators import exclude_validator
from users.models import User


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['name',
                  'owner',
                  'place',
                  'time',
                  'action',
                  'is_pleasure',
                  'associated_habits',
                  'periodic',
                  'award',
                  'time_exec',
                  'is_public'
                  ]
        validators = [exclude_validator, ]


class HabitListSerializer(serializers.ModelSerializer):
    owner = SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Habit
        fields = ['name',
                  'owner',
                  'place',
                  'time',
                  'action',
                  'is_pleasure',
                  'associated_habits',
                  'periodic',
                  'award',
                  'time_exec',
                  'is_public'
                  ]
