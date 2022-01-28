from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from django.conf import settings

slack_token = settings.SLACKO_BOT_USER_OATH_TOKEN
client = WebClient(token=slack_token)

try:
    response = client.chat_postMessage(channel='#chores', text='okay :cry:')
except SlackApiError as e:
    assert e.response["error"]


# justine
# U02UFNL52MS

#joe
# U02UFNHJAJ0
~                         
