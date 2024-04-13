import time
import requests
from celery import shared_task
from track_habits.settings import TG_URL, TG_BOT_TOKEN
from habits.models import Habit


class MyBot:
    URL = TG_URL
    TOKEN = TG_BOT_TOKEN

    def send_message(self, tg_id, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': tg_id,
                'text': text
            }
        )


@shared_task
def habits_bot():
    my_bot = MyBot()
    habits = Habit.objects.all()
    for habit in habits:

        owner = habit.owner
        if owner is None:
            continue
        tg_id = owner.id_tg
        if tg_id is None:
            continue

        action = habit.action
        time_habit = habit.time
        place = habit.place
        time_exec = habit.time_exec.strftime("%H:%M:%S")
        if time_exec is None:
            time_exec = "00:02"
        time_sec = sum(x * int(t) for x, t in
                       zip([3600, 60, 1], time_exec.split(":")))
        text = (f'Я должен {action} в {time_habit} в {place} выполнять '
                f'{time_sec} '
                f'секунд.')
        my_bot.send_message(tg_id, text)

        time.sleep(time_sec)
        if habit.award is not None:
            text = f'Вознаграждение {habit.award}'
            my_bot.send_message(tg_id, text)
