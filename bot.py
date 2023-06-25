import os
import logging
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from flask import Flask, request

logging.basicConfig(level=logging.DEBUG)

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])


handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
handler.connect()

flask_app = Flask(__name__)

@flask_app.route("/", methods=["GET"])
def index():
    return "Hello World"


# @app.command("/p")
# def repeat_text(ack, respond, command):
#     ack()
#     respond(f"{command['text']}")

@app.message(".*")
def message_handler(message, say, logger):
    print(message)

    say("output")

@app.event("app_mention")
def mention_handler(body, say):
    say('Hello World!')

