#載入LineBot所需要的模組 
from flask import Flask, request, abort  
from linebot import (LineBotApi, WebhookHandler) 
from linebot.exceptions import (InvalidSignatureError) 
from linebot.models import *
app = Flask(__name__)  
# 必須放上自己的Channel Access Token 
line_bot_api = LineBotApi('Yl+OCwFl+sqIFHYOHlUKjiFF0uAmMS0spBsH4UzwRERlKkDiTWLyDE02fTZtnSEJiPwR8ikyFSn0kaXNCmm3jXZUA+MD8Am0YbtaYk3U4b7kr/B7sUo+mP+UqHVcrz1N5bhhNfof+gO3t0/cNV9ROwdB04t89/1O/w1cDnyilFU=')  
# 必須放上自己的Channel Secret
handler = WebhookHandler('83e83985799c58bebf796b54406be6cb')
line_bot_api.push_message('U03c641f73d89933c2580b5c5a96ed50e', TextSendMessage(text='你可以開始了'))
# 監聽所有來自 /callback 的 Post Request 
@app.route("/callback", methods=['POST']) 
def callback():     
# get X-Line-Signature header value     
signature = request.headers['X-Line-Signature']
# get request body as text     
body = request.get_data(as_text=True)     
app.logger.info("Request body: " + body)      
# handle webhook body     
try:         handler.handle(body, signature)     
except InvalidSignatureError:         abort(400)      
return 'OK'
