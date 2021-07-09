import logging
logging.basicConfig(level=logging.DEBUG)
import os 
import re
from slack_bolt import App, Ack, Say, BoltContext
from slack_bolt.adapter.socket_mode import SocketModeHandler



# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])


'''Slack Test: /build testserver'''
@app.command("/build")
def build_command(ack, body):
    user_id = body["user_id"]
    text = body["text"]
    ack(f"Hi <@{user_id}>!. Deploying [{text}] Server Now")


'''Slack Test: @infracid-app are you there'''
@app.event("app_mention")
def event_test(event, say):
    say(f"Hi there, <@{event['user']}>!")


''' Your listener will be called every time a block element with callback_id "test_deploy" is triggered'''
@app.action("test_deploy")
def handle_some_action(ack, body, logger, respond, action):
    ack()
    #logger.info(body)
    response = body['actions'][0]['value']
    if response == 'yes':
       respond(f"You selected {response}. Request approved 👍")
    else:
       respond(f"You selected {response}. Request approved :thumbsdown:") 



if __name__ == "__main__":
    # export SLACK_APP_TOKEN=xapp-***
    # export SLACK_BOT_TOKEN=xoxb-***
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
    #handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    #handler.start()
