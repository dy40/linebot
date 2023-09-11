from flask import Flask, abort, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# 填入你的 message api 資訊
line_bot_api = LineBotApi('iE3s9yZUJxT+bSfx9B9n38HlvQ7gIyIk9R1ky0R7aOWvwkLJa9Wj7ZfJSDwQ0uIzrAV7fiXfvWbvPKUEOkmY5O3hgITPXVBY/YQGGRPN51FIaxU0ukPdxutYnFsbfWX7h6XV/y9lDnQfQQ2uDa03LwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1abd8430f844df55d0d365ec352c828c')

# 設定你接收訊息的網址，如 https://YOURAPP.herokuapp.com/callback
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body, "Signature: " + signature)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("Handle: reply_token: " + event.reply_token + ", message: " + event.message.text)
    content = "{}: {}".format(event.source.user_id, event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=content))

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])