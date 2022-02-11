from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import datetime
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from do_your_chores.models import Week, Day, TaskList, AssignedTask, Member


#try:
#    response = client.chat_postMessage(channel='#chores', text='okay :cry:')
#except SlackApiError as e:
#    assert e.response["error"]

class Command(BaseCommand):
    help = 'Checks the current day for tasks and then notifies household members of their tasks for the day'

    def handle(self, *args, **kwargs):
        
        this_week = Week.objects.latest()
        today_iso = datetime.date.today().isoweekday()
        today = Day.objects.get(day=today_iso,week=this_week)
        todays_chores = AssignedTask.objects.filter(day__week=this_week,day=today)

        #slack_token = settings.SLACK_BOT_USER_OATH_TOKEN
        client = WebClient(token='xoxb-2965492515603-2984605078993-dWZuPOegc7ShTTVWAL8OXQmL')
       



        for i in todays_chores:
            message = 'Assigned Chore: {}'.format(i.name)
            try:
                response = client.chat_postMessage(channel=i.owner.slack_memberid, text=message)
            except SlackApiError as e:
                assert e.response["error"]
            print(i.owner.slack_memberid)
            #to_assign = Member.objects.get(name=i.owner)
            #print(to_assign)





#latest_tasks = AssignedTask.objects.filter(day__week__pk=new_week.pk)




# justine
# U02UFNL52MS

#joe
# U02UFNHJAJ0
