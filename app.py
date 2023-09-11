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
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))
# Channel Secret
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))





# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def handle_message(event):
    mtext = event.message.text
    if mtext == '@確診後流程':
        try:
            message = [
                TextSendMessage( #傳文字
                text = "確診後該怎麼辦?(SOP圖示)"
                ),
                ImageSendMessage( #傳圖片
                    original_content_url="https://ithelp.ithome.com.tw/upload/images/20220925/20151681EaMkK6ROvq.jpg",
                    preview_image_url="https://ithelp.ithome.com.tw/upload/images/20220925/20151681EaMkK6ROvq.jpg"
                ),
                TextSendMessage(  # 傳文字
                    text="小叮嚀: \n \n @因為看線上中醫的程序與需要等待的時間較久, 若想要中西藥都一起吃的話, 可以拿到西藥後 (比較快), 打電話請附近中藥行代煮**清冠一號***的水藥或磨成藥粉先吃, 再花時間處理看中醫需申請的證明, 程序等等...(若已有清冠一號後, 看中醫前, 可以參考圖文選單中間下面的**關於屁桃** > 看中/西醫的小訣竅) \n \n @中藥行的代煮清冠一號, 會請顧客到 **維基百科** 截圖中藥材的配方, 並傳至Line 上請他們代煮水藥或磨成藥粉 (水藥和藥粉的差異請點選 圖文選單中間下面的**關於屁桃** > 確診保養相關資訊)"
                )]
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token,
                TextSendMessage(text= 'Sorry~屁桃故障囉！'))
    elif mtext == '@想看西藥＆拿西藥':
        try:
            message = ImageSendMessage(
                original_content_url = "https://ithelp.ithome.com.tw/upload/images/20220925/20151681EaMkK6ROvq.jpg",
                preview_image_url = "https://ithelp.ithome.com.tw/upload/images/20220925/20151681EaMkK6ROvq.jpg"
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token,
                TextSendMessage(text= 'Sorry~屁桃故障囉！'))
    elif mtext == '@想看中藥＆拿中藥':
        try:
            message = StickerSendMessage(
                package_id = '8522',
                sticker_id = '16581289'
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token,
                TextSendMessage(text= 'Sorry~屁桃故障囉！'))



        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)