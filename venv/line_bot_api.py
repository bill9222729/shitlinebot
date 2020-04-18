from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, FollowEvent, PostbackEvent, TemplateSendMessage, ButtonsTemplate, ImageSendMessage, PostbackAction, URIAction, MessageAction, FlexSendMessage)

line_bot_api = LineBotApi('9gEcD6pNZWA9xe65jwSrzzykJnBNYhgBdqaUDpvafeMTyG0D+LELBnV/53HwYiue8bTWswthp0SjGEOzGy8UroCrCpfs2WWwbjGynTVFzJIjFYq2dAJZpDDXPqf5ki46kWvQbmmfCl9O58pb2QFFEQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('acbb4e00d0ca2c5bb69cdb4109b6fbf2')