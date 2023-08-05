#載入LineBot所需要的模組 
from flask import Flask, request, abort  
from linebot import (LineBotApi, WebhookHandler) 
from linebot.exceptions import (InvalidSignatureError) 
from linebot.models import *
#訊息傳遞區塊 

#訊息傳遞區塊 
##### 基本上程式編輯都在這個function ##### 
@handler.add(MessageEvent, message=TextMessage) 
def handle_message(event):     
 message = event.message.text     
line_bot_api.reply_message(event.reply_token,TextSendMessage(message))

#主程式 
import os if __name__ == "__main__":    
 port = int(os.environ.get('PORT', 5000))     
app.run(host='0.0.0.0', port=port)






