from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

#config模組方案
from config import * 

line_bot_api = LineBotApi("ubteHqNvcMBz9cw2xlQxNtMKlRKD1VNbVA1/HKU6MI6p3YEmN2CmGMP1GM7Wg8eyiPwR8ikyFSn0kaXNCmm3jXZUA+MD8Am0YbtaYk3U4b59YWEGwQQBEic356Xr+cXs4BhXrLKJ1ptvxV5rDkzoY wdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("83e83985799c58bebf796b54406be6cb")


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    #get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    #handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.source.user_id =='Udeadbeefdeadbeefdeadbeefdeadbeef':
        return 'OK'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
  