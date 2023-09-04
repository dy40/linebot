from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

from googletrans import Translator

app = Flask(__name__)

from config import * 

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


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

def translate_text(text,dest='en'):
    """以google翻譯將text翻譯為目標語言

    :param text: 要翻譯的字串，接受UTF-8編碼。
    :param dest: 要翻譯的目標語言，參閱googletrans.LANGCODES語言列表。
    """
    translator = Translator()
    result = translator.translate(text, dest).text
    return result

import mplfinance as mpf
import yfinance as yf
# import pandas_datareader.data as web
import pyimgur

IMGUR_CLIENT_ID = imgur_client_id

def plot_stcok_k_chart(IMGUR_CLIENT_ID,stock="0050" , date_from='2020-01-01' ):
    """
    進行個股K線繪製，回傳至於雲端圖床的連結。將顯示包含5MA、20MA及量價關係，起始預設自2020-01-01起迄昨日收盤價。
    :stock :個股代碼(字串)，預設0050。
    :date_from :起始日(字串)，格式為YYYY-MM-DD，預設自2020-01-01起。
    """
    stock = str(stock)+".tw"
    # df = web.DataReader(stock, 'yahoo', date_from) 
    df = yf.download(stock, date_from) 
    mpf.plot(df,type='candle',mav=(5,20),volume=True, ylabel=stock.upper()+' Price' ,savefig='testsave.png')
    PATH = "testsave.png"
    im = pyimgur.Imgur(IMGUR_CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title=stock+" candlestick chart")
    return uploaded_image.link

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.source.user_id =='Udeadbeefdeadbeefdeadbeefdeadbeef':
        return 'OK'
    if event.message.text[:3] == "@翻英":
        content = translate_text(event.message.text[3:], "en")
        message = TextSendMessage(text=content)
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text[:3] == "@翻日":
        content = translate_text(event.message.text[3:] , "ja")
        message = TextSendMessage(text=content)
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text[:3] == "@翻中":
        content = translate_text(event.message.text[3:] , "zh-tw")
        message = TextSendMessage(text=content)
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text[:2].upper() == "@K":
        input_word = event.message.text.replace(" ","") #合併字串取消空白
        stock_name = input_word[2:6] #2330
        start_date = input_word[6:] #2020-01-01
        content = plot_stcok_k_chart(IMGUR_CLIENT_ID,stock_name,start_date)
        message = ImageSendMessage(original_content_url=content,preview_image_url=content)
        line_bot_api.reply_message(event.reply_token, message)

    else: line_bot_api.reply_message(event.reply_token,
                                     TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()