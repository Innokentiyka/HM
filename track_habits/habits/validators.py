from rest_framework import serializers
from datetime import time


def exclude_validator(value):
    if value.get('assoc_habit') and value.get('award'):
        raise serializers.ValidationError('Исключён одновременный выбор '
                                          'связанной привычки и указания '
                                          'вознаграждения.')
    if value.get('time_exec') and value.get('time_exec') > time(00, 2):
        raise serializers.ValidationError('Время выполнения должно быть '
                                          'не больше 120 секунд.')
    if 'assoc_habit' in value and value.get('assoc_habit').is_pleasure:
        raise serializers.ValidationError('В связанные привычки могут попадать'
                                          ' только привычки с признаком '
                                          'приятной привычки.')
    if value.get('is_pleasure') and value.get('award'):
        raise serializers.ValidationError('У приятной привычки не может быть '
                                          'вознаграждения или связанной '
                                          'привычки.')
    if value.get('periodic') and value.get('periodic') > 7:
        raise serializers.ValidationError('Нельзя выполнять привычку реже, '
                                          'чем 1 раз в 7 дней.')
