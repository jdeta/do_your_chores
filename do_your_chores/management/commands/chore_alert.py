from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import datetime
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from do_your_chores.models import Week, Day, TaskList, AssignedTask, Member

slack_token = settings.SLACKO_BOT_USER_OATH_TOKEN
client = WebClient(token=slack_token)

#try:
#    response = client.chat_postMessage(channel='#chores', text='okay :cry:')
#except SlackApiError as e:
#    assert e.response["error"]

class Command(BaseCommand):
    help = 'Checks the current day for tasks and then notifies household members of their tasks for the day'

    def handle(self, *args, **kwargs):
        today_iso = datetime.date.today().isoweekday()
        AssignedTask.objects.filter(day=today_iso).filter(week=







# justine
# U02UFNL52MS

#joe
# U02UFNHJAJ0
~                         
