from __future__ import unicode_literals

import random
import time
from datetime import timedelta, datetime
from pymongo import MongoClient

#ref: http://twstock.readthedocs.io/zh_TW/latest/quickstart.html#id2
import twstock

import matplotlib
matplotlib.use('Agg') # ref: https://matplotlib.org/faq/howto_faq.html
import matplotlib.pyplot as plt
import pandas as pd

from imgurpython import ImgurClient

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)


channel_secret_8 = 'your channel_secret'
channel_access_token_8 = 'your channel_access_token'
line_bot_api_8 = LineBotApi(channel_access_token_8)
parser_8 = WebhookParser(channel_secret_8)


#===================================================
#   stock bot
#===================================================
@app.route("/callback_yangbot8", methods=['POST'])
def callback_yangbot8():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser_8.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)

line_bot_api = LineBotApi('channl access token')
handler = WebhookHandler('secrect key ')
my_user_id = 'Your UserID'
line_bot_api.push_message(my_user_id, TextSendMessage(text="start"))
@app.route("/")
def home():
    return "home"
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = str(event.message.text).upper().strip() # 使用者輸入的內容
    profile = line_bot_api.get_profile(event.source.user_id)
    user_name = profile.display_name #使用者名稱
    uid = profile.user_id # 發訊者ID
#================================ 
    # 問卷
    if re.match("問卷分析", msg):
        line_bot_api.push_message(uid, TextSendMessage(questionnaire.greeting_msg))
        line_bot_api.push_message(uid, TextSendMessage(questionnaire.Q1))
        content = questionnaire.Q1_menu()
        line_bot_api.push_message(uid, content)
        return 0
    elif re.match("Q2", msg):
        line_bot_api.push_message(uid, TextSendMessage(questionnaire.Q2))
        line_bot_api.push_message(uid, questionnaire.Q2_menu())
        return 0
    elif re.match("Q3", msg):
        line_bot_api.push_message(uid, TextSendMessage(questionnaire.Q3))
        line_bot_api.push_message(uid, questionnaire.Q3_menu())
        return 0
    elif re.match("Q4", msg):
        line_bot_api.push_message(uid, TextSendMessage(questionnaire.Q4))
        line_bot_api.push_message(uid, questionnaire.Q4_menu())
        return 0
    elif re.match("Q5", msg):
        line_bot_api.push_message(uid, TextSendMessage(questionnaire.Q5))
        line_bot_api.push_message(uid, questionnaire.Q5_menu())
        return 0
    elif re.match("Q6", msg):
        line_bot_api.push_message(uid, TextSendMessage(questionnaire.Q6))
        line_bot_api.push_message(uid, questionnaire.Q6_menu())
        return 0
    elif re.match("Q7", msg):
        line_bot_api.push_message(uid, TextSendMessage(questionnaire.Q7))
        line_bot_api.push_message(uid, questionnaire.Q7_menu())
        return 0
    elif re.match("Q8", msg):
        line_bot_api.push_message(uid, TextSendMessage(questionnaire.Q8))
        line_bot_api.push_message(uid, questionnaire.Q8_menu())
        return 0
    elif re.match("類型A", msg):
        img_url = questionnaire.type_A
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型B", msg):
        img_url = questionnaire.type_B
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型B", msg):
        img_url = questionnaire.type_B
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型C", msg):
        img_url = questionnaire.type_C
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型D", msg):
        img_url = questionnaire.type_D
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型E", msg):
        img_url = questionnaire.type_E
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型F", msg):
        img_url = questionnaire.type_F
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型G", msg):
        img_url = questionnaire.type_G
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型H", msg):
        img_url = questionnaire.type_H
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型I", msg):
        img_url = questionnaire.type_I
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0
    elif re.match("類型J", msg):
        img_url = questionnaire.type_J
        line_bot_api.push_message(uid, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return 0



        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)