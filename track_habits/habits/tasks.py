from celery import shared_task

from habits.services import habits_bot


@shared_task
def habit_reminders():
    habits_bot()
