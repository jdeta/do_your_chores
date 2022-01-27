
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from django.conf import settings

slack_token = 'xoxb-2965492515603-2984605078993-kO4FmcRsY9I2h1546idOWm1x'
client = WebClient(token=slack_token)

#try:
#    response = client.chat_postMessage(channel='#chores', text='okay :cry:')
#except SlackApiError as e:
#    assert e.response["error"]


try:
    response = client.chat_postMessage(channel='U02UFNL52MS', text='We are not able to converse (yet), so if you try to message me, I will not be able to respond')
except SlackApiError as e:
    assert e.response["error"]




# justine
# U02UFNL52MS

#joe
# U02UFNHJAJ0
