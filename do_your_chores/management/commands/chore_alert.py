from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import datetime
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from do_your_chores.models import Week, Day, TaskList, AssignedTask, Member

class Command(BaseCommand):
    help = 'Checks the current day for tasks and then notifies household members of their tasks for the day'

    def handle(self, *args, **kwargs):
        
        this_week = Week.objects.latest()
        today_iso = datetime.date.today().isoweekday()
        today = Day.objects.get(day=today_iso,week=this_week)
        todays_weekly_chores = AssignedTask.objects.filter(day__week=this_week,day=today,frequency=2)
        todays_daily_chores = AssignedTask.objects.filter(day__week=this_week,day=today,frequency=1)

        client = WebClient(token=''.join(settings.SLACK_BOT_USER_OATH_TOKEN))
       
        for i in todays_daily_chores:
            message = 'Daily reminder to {}'.format(i.name)
            try:
                response = client.chat_postMessage(channel='#chores',text=message)
            except SlackApiError as e:
                assert e.response["error"]



        for i in todays_weekly_chores:
            message = 'Assigned Chore: {}'.format(i.name)
            try:
                response = client.chat_postMessage(channel=i.owner.slack_memberid, text=message)
            except SlackApiError as e:
                assert e.response["error"]
