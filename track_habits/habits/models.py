from django.db import models

from users.models import User


class Habit(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              verbose_name='создатель',
                              related_name='owner')
    place = models.CharField(max_length=200, verbose_name='место')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=200, verbose_name='действие')
    is_pleasure = models.BooleanField(default=True,
                                      verbose_name='признак приятной привычки')
    associated_habits = models.ForeignKey('self', on_delete=models.SET_NULL,
                                          blank=True, null=True,
                                          verbose_name='связанная привычка',
                                          related_name='habits_associated')
    periodic = models.IntegerField(default=1,
                                   verbose_name='периодичность в днях')
    award = models.CharField(max_length=150, verbose_name='вознаграждение',
                             blank=True, null=True, )
    time_exec = models.TimeField(verbose_name='время на выполнение',
                                 default='00:02',
                                 blank=True, null=True, )
    is_public = models.BooleanField(default=True,
                                    verbose_name='признак публичности')

    def __str__(self):
        return f'{self.name} {self.action}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ['name', 'place', 'action']
