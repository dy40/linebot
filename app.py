from flask import Flask
app = Flask(__name__)

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage,TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction

line_bot_api = LineBotApi('ZuqEf8yqUPeYP0Ekr9Q3tiv0fy5MVa7MUa9m/BuM9e1M3VBHRBEUjdSIz+Fesg+lzzqz05VbZTasXaWpDwcc3sJi10gft4S9cSMHDQ79jAum51T3qUPwrRzLIiugzovRQceNJ4ro67sVmtihY9lUUAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3b121dfe3eadcd614bd6bd10cb18f0ca')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
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

if __name__ == '__main__':
    app.run()