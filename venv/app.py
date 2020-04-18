from flask import Flask, request, abort
from models.users import User
from line_bot_api import *
from database import db_session, init_db
from record_message import record_message_event
from rich_menu import richmenu_list, start_richmenu
import buttonsTemplate
import re

app = Flask(__name__)


@app.before_first_request
def init():
    init_db()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print(body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #綁webhook
    if event.reply_token == '00000000000000000000000000000000' :
        return 'ok'
    user_id = event.source.user_id
    user_name = line_bot_api.get_profile(event.source.user_id).display_name
    user = User.query.filter(User.id == user_id).first()
    query = User.query.filter_by(id=user_id).first()
    if not user:
        user = User(id=user_id, user_name=user_name)
        print(user)
        db_session.add(user)
        db_session.commit()
    elif user.is_signup:
        content = event.message.text
        correct_cellphone_number = re.match(r'(?:0|886-?)9\d{2}-?\d{6}', content)
        if correct_cellphone_number:
            line_bot_api.push_message(user_id, TextSendMessage('恭喜註冊成功！'))
            start_richmenu.setRichmenu(richmenu_list.RichMenu_ID.richmenu_07)
            query.is_member = True
            query.is_signup = False
            query.phone_number = content
            db_session.commit()
            return
        else:
            line_bot_api.push_message(user_id, FlexSendMessage(alt_text='aa',
                                                               contents={
                                                                   "type": "bubble",
                                                                   "footer": {
                                                                       "type": "box",
                                                                       "layout": "vertical",
                                                                       "contents": [
                                                                           {
                                                                               "type": "text",
                                                                               "text": "錯誤的手機格式",
                                                                               "size": "lg",
                                                                               "weight": "bold",
                                                                               "offsetStart": "10px",
                                                                               "offsetTop": "5px"
                                                                           },
                                                                           {
                                                                               "type": "text",
                                                                               "text": "正確的手機格式應該是0988111222",
                                                                               "wrap": True,
                                                                               "size": "md",
                                                                               "decoration": "none",
                                                                               "margin": "sm",
                                                                               "offsetEnd": "10px",
                                                                               "offsetStart": "10px",
                                                                               "offsetTop": "5px"
                                                                           },
                                                                           {
                                                                               "type": "button",
                                                                               "action": {
                                                                                   "type": "postback",
                                                                                   "label": "取消輸入",
                                                                                   "data": "exit"
                                                                               },
                                                                               "margin": "md",
                                                                               "offsetTop": "5px"
                                                                           }
                                                                       ]
                                                                   }
                                                               }))
    elif not query.is_member:
        print('in')
        start_richmenu.setRichmenu(richmenu_list.RichMenu_ID.richmenu_03)
        line_bot_api.push_message(user_id, FlexSendMessage(alt_text='還沒加入我們?',
                                                           contents={
                                                               "type": "bubble",
                                                               "footer": {
                                                                   "type": "box",
                                                                   "layout": "vertical",
                                                                   "contents": [
                                                                       {
                                                                           "type": "text",
                                                                           "text": "還沒加入我們?",
                                                                           "size": "lg",
                                                                           "weight": "bold",
                                                                           "offsetStart": "10px",
                                                                           "offsetTop": "5px"
                                                                       },
                                                                       {
                                                                           "type": "text",
                                                                           "text": "嗨，你好像還沒加入我們，趕快加\n入我們體驗更多完整的服務吧！",
                                                                           "wrap": True,
                                                                           "size": "md",
                                                                           "decoration": "none",
                                                                           "margin": "sm",
                                                                           "offsetEnd": "10px",
                                                                           "offsetStart": "10px",
                                                                           "offsetTop": "5px"
                                                                       },
                                                                       {
                                                                           "type": "button",
                                                                           "action": {
                                                                               "type": "postback",
                                                                               "label": "加入我們",
                                                                               "data": "join_us",
                                                                               "displayText": "好阿阿"
                                                                           },
                                                                           "margin": "md",
                                                                           "offsetTop": "5px"
                                                                       }
                                                                   ]
                                                               }
                                                           }))
    elif query.is_member:
        print('out')
        print(query.is_member)
        print(query.is_signup)
        start_richmenu.setRichmenu(richmenu_list.RichMenu_ID.richmenu_07)
    record_message_event(event)
    # 更換RICHMENU測試
    if event.message.text == 'change1':
        start_richmenu.setRichmenu(richmenu_list.RichMenu_ID.richmenu_01)
    elif event.message.text == 'change2':
        start_richmenu.setRichmenu(richmenu_list.RichMenu_ID.richmenu_02)
    elif event.message.text == 'change3':
        start_richmenu.setRichmenu(richmenu_list.RichMenu_ID.richmenu_03)
    elif event.message.text == 'change4':
        start_richmenu.setRichmenu(richmenu_list.RichMenu_ID.richmenu_04)
    elif event.message.text == 'change5':
        start_richmenu.setRichmenu(richmenu_list.RichMenu_ID.richmenu_05)
    elif event.message.text == 'change6':
        start_richmenu.setRichmenu(richmenu_list.RichMenu_ID.richmenu_06)
    elif event.message.text == 'change7':
        start_richmenu.setRichmenu(richmenu_list.RichMenu_ID.richmenu_07)
    # 發送訊息
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=event.message.text))

    if event.message.text == '編輯使用者名稱':
        query.edit_user_name = True
        query.edit_home_address = False
        query.edit_company_address = False
        db_session.commit()
        line_bot_api.push_message(user_id, FlexSendMessage(alt_text='編輯使用者名稱',
                                                           contents={
                                                               "type": "bubble",
                                                               "footer": {
                                                                   "type": "box",
                                                                   "layout": "vertical",
                                                                   "contents": [
                                                                       {
                                                                           "type": "text",
                                                                           "text": "該如何稱呼你？",
                                                                           "size": "lg",
                                                                           "weight": "bold",
                                                                           "offsetStart": "10px",
                                                                           "offsetTop": "5px"
                                                                       },
                                                                       {
                                                                           "type": "text",
                                                                           "text": "取個好的名稱方便老闆認出你！你\n也可以隨時更換名稱",
                                                                           "wrap": True,
                                                                           "size": "md",
                                                                           "decoration": "none",
                                                                           "margin": "sm",
                                                                           "offsetEnd": "10px",
                                                                           "offsetStart": "10px",
                                                                           "offsetTop": "5px"
                                                                       },
                                                                       {
                                                                           "type": "button",
                                                                           "action": {
                                                                               "type": "postback",
                                                                               "label": "取消輸入",
                                                                               "data": "exit"
                                                                           },
                                                                           "margin": "md",
                                                                           "offsetTop": "5px"
                                                                       }
                                                                   ]
                                                               }
                                                           }))
        return
    elif event.message.text == '編輯住家':
        query.edit_user_name = False
        query.edit_home_address = True
        query.edit_company_address = False
        db_session.commit()
        line_bot_api.push_message(user_id, FlexSendMessage(alt_text='編輯住家',
                                                           contents={
                                                               "type": "bubble",
                                                               "footer": {
                                                                   "type": "box",
                                                                   "layout": "vertical",
                                                                   "contents": [
                                                                       {
                                                                           "type": "text",
                                                                           "text": "你住哪裡？",
                                                                           "size": "lg",
                                                                           "weight": "bold",
                                                                           "offsetStart": "10px",
                                                                           "offsetTop": "5px"
                                                                       },
                                                                       {
                                                                           "type": "text",
                                                                           "text": "設定一個住址或是大地標，下次出門\n就能快速買早餐",
                                                                           "wrap": True,
                                                                           "size": "md",
                                                                           "decoration": "none",
                                                                           "margin": "sm",
                                                                           "offsetEnd": "10px",
                                                                           "offsetStart": "10px",
                                                                           "offsetTop": "5px"
                                                                       },
                                                                       {
                                                                           "type": "button",
                                                                           "action": {
                                                                               "type": "postback",
                                                                               "label": "取消輸入",
                                                                               "data": "exit"
                                                                           },
                                                                           "margin": "md",
                                                                           "offsetTop": "5px"
                                                                       }
                                                                   ]
                                                               }
                                                           }))
        return
    elif event.message.text == '編輯公司':
        query.edit_user_name = False
        query.edit_home_address = False
        query.edit_company_address = True
        db_session.commit()
        line_bot_api.push_message(user_id, FlexSendMessage(alt_text='編輯公司',
                                                           contents={
                                                               "type": "bubble",
                                                               "footer": {
                                                                   "type": "box",
                                                                   "layout": "vertical",
                                                                   "contents": [
                                                                       {
                                                                           "type": "text",
                                                                           "text": "你在哪裡上班？",
                                                                           "size": "lg",
                                                                           "weight": "bold",
                                                                           "offsetStart": "10px",
                                                                           "offsetTop": "5px"
                                                                       },
                                                                       {
                                                                           "type": "text",
                                                                           "text": "設定一個公司地址或是大地標，下次\n上班前就能快速買早餐",
                                                                           "wrap": True,
                                                                           "size": "md",
                                                                           "decoration": "none",
                                                                           "margin": "sm",
                                                                           "offsetEnd": "10px",
                                                                           "offsetStart": "10px",
                                                                           "offsetTop": "5px"
                                                                       },
                                                                       {
                                                                           "type": "button",
                                                                           "action": {
                                                                               "type": "postback",
                                                                               "label": "取消輸入",
                                                                               "data": "exit"
                                                                           },
                                                                           "margin": "md",
                                                                           "offsetTop": "5px"
                                                                       }
                                                                   ]
                                                               }
                                                           }))
        return

    if query.edit_user_name:
        print('編輯使用者中')
        query.user_name = event.message.text
        query.edit_user_name = False
        db_session.commit()
        line_bot_api.push_message(user_id, TextSendMessage(text='設定完成'))
    elif query.edit_home_address:
        print('編輯住家中')
        query.home_address = event.message.text
        query.edit_home_address = False
        db_session.commit()
        line_bot_api.push_message(user_id, TextSendMessage(text='設定完成'))
    elif query.edit_company_address:
        print('編輯公司中')
        query.company_address = event.message.text
        query.edit_company_address = False
        db_session.commit()
        line_bot_api.push_message(user_id, TextSendMessage(text='設定完成'))


@handler.add(FollowEvent)
def follow_message(event):
    user_id = event.source.user_id
    user_name = line_bot_api.get_profile(event.source.user_id).display_name
    user = User.query.filter(User.id == user_id).first()
    if not user:
        user = User(id=user_id, user_name=user_name)
        print(user)
        db_session.add(user)
        db_session.commit()
    start_richmenu.setRichmenu(richmenu_list.RichMenu_ID.richmenu_03)
    print('welcome')
    line_bot_api.reply_message(
        event.reply_token,
        FlexSendMessage(alt_text='welcome',
                        contents={
                            "type": "bubble",
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "嗨，歡迎加入我們",
                                        "size": "lg",
                                        "weight": "bold",
                                        "offsetStart": "10px",
                                        "offsetTop": "5px"
                                    },
                                    {
                                        "type": "text",
                                        "text": "嗨，我是屎蛋，我不只會訂餐，還會幫你\n做很多事情ㄛ！先加入我們體驗更完善的\n服務吧！",
                                        "wrap": True,
                                        "size": "sm",
                                        "decoration": "none",
                                        "margin": "sm",
                                        "offsetEnd": "10px",
                                        "offsetStart": "10px",
                                        "offsetTop": "5px"
                                    },
                                    {
                                        "type": "button",
                                        "action": {
                                            "type": "postback",
                                            "label": "加入我們",
                                            "data": "join_us",
                                            "displayText": "好阿阿"
                                        },
                                        "margin": "md",
                                        "style": "primary",
                                        "offsetTop": "5px",
                                        "position": "relative",
                                        "height": "sm"
                                    }
                                ]
                            }
                        })
    )


@handler.add(PostbackEvent)
def handle_postback(event):
    user_id = event.source.user_id
    query = User.query.filter_by(id=user_id).first()
    if event.postback.data == 'join_us':
        # 資料庫該使用者狀態改為註冊中
        # Updata data
        query.is_signup = True
        print(query.is_signup)
        db_session.commit()

        line_bot_api.push_message(user_id, FlexSendMessage(
            alt_text='還沒加入我們?',
            contents={
                "type": "bubble",
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "輸入手機號碼",
                            "size": "lg",
                            "weight": "bold",
                            "offsetTop": "5px",
                            "offsetStart": "10px"
                        },
                        {
                            "type": "text",
                            "text": "我們利用手機號碼驗證您的身分，\n並於必要時聯絡使用",
                            "margin": "sm",
                            "size": "md",
                            "wrap": True,
                            "decoration": "none",
                            "offsetTop": "5px",
                            "offsetStart": "10px",
                            "offsetEnd": "10px"
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "postback",
                                "label": "取消輸入",
                                "data": "exit"
                            },
                            "margin": "md",
                            "offsetTop": "5px"
                        }
                    ]
                }
            }
        ))
    elif event.postback.data == 'exit':
        query.is_signup = False
        query.edit_user_name = False
        query.edit_home_address = False
        query.edit_company_address = False
        db_session.commit()
        line_bot_api.push_message(user_id, TextSendMessage(text='好的，歡迎您再來找我聊聊天喔！'))
    elif event.postback.data == '附近店家':
        line_bot_api.push_message(user_id, TextSendMessage(text='附近店家還沒開'))
    elif event.postback.data == '快速選單':
        line_bot_api.push_message(user_id, TextSendMessage(text='快速選單還沒做好'))
    elif event.postback.data == '小幫手':
        line_bot_api.push_message(user_id, TextSendMessage(text='小幫手還在睡'))
    elif event.postback.data == '搜尋':
        line_bot_api.push_message(user_id, TextSendMessage(text='功能還沒做好啦'))
    elif event.postback.data == '老樣子':
        line_bot_api.push_message(user_id, TextSendMessage(text='誰知道你老樣子'))
    elif event.postback.data == '會員中心':
        line_bot_api.push_message(user_id, TextSendMessage(text='這是專屬於你的會員中心'))
        line_bot_api.push_message(user_id, FlexSendMessage(alt_text='這是專屬於你的會員中心',
                                                           contents={
                                                               "type": "carousel",
                                                               "contents": [
                                                                   {
                                                                       "type": "bubble",
                                                                       "hero": {
                                                                           "type": "image",
                                                                           "url": "https://i.imgur.com/bZtyoDh.jpg",
                                                                           "aspectRatio": "20:13",
                                                                           "size": "full",
                                                                           "aspectMode": "cover"
                                                                       },
                                                                       "body": {
                                                                           "type": "box",
                                                                           "layout": "vertical",
                                                                           "contents": [
                                                                               {
                                                                                   "type": "text",
                                                                                   "text": "你的名稱",
                                                                                   "weight": "bold"
                                                                               },
                                                                               {
                                                                                   "type": "text",
                                                                                   "text": "{}".format(query.user_name),
                                                                                   "offsetTop": "10px"
                                                                               }
                                                                           ],
                                                                           "height": "130px"
                                                                       },
                                                                       "footer": {
                                                                           "type": "box",
                                                                           "layout": "vertical",
                                                                           "contents": [
                                                                               {
                                                                                   "type": "button",
                                                                                   "action": {
                                                                                       "type": "message",
                                                                                       "label": "點我編輯",
                                                                                       "text": "編輯使用者名稱"
                                                                                   }
                                                                               }
                                                                           ]
                                                                       }
                                                                   },
                                                                   {
                                                                       "type": "bubble",
                                                                       "hero": {
                                                                           "type": "image",
                                                                           "url": "https://i.imgur.com/FxZtHz0.jpg",
                                                                           "aspectRatio": "20:13",
                                                                           "size": "full",
                                                                           "aspectMode": "cover"
                                                                       },
                                                                       "body": {
                                                                           "type": "box",
                                                                           "layout": "vertical",
                                                                           "contents": [
                                                                               {
                                                                                   "type": "text",
                                                                                   "text": "你的住家",
                                                                                   "weight": "bold"
                                                                               },
                                                                               {
                                                                                   "type": "text",
                                                                                   "text": "{}".format(
                                                                                       query.home_address),
                                                                                   "offsetTop": "10px"
                                                                               }
                                                                           ],
                                                                           "height": "130px"
                                                                       },
                                                                       "footer": {
                                                                           "type": "box",
                                                                           "layout": "vertical",
                                                                           "contents": [
                                                                               {
                                                                                   "type": "button",
                                                                                   "action": {
                                                                                       "type": "message",
                                                                                       "label": "點我編輯",
                                                                                       "text": "編輯住家"
                                                                                   }
                                                                               }
                                                                           ]
                                                                       }
                                                                   },
                                                                   {
                                                                       "type": "bubble",
                                                                       "hero": {
                                                                           "type": "image",
                                                                           "url": "https://i.imgur.com/NaqdvcT.jpg",
                                                                           "aspectRatio": "20:13",
                                                                           "size": "full",
                                                                           "aspectMode": "cover"
                                                                       },
                                                                       "body": {
                                                                           "type": "box",
                                                                           "layout": "vertical",
                                                                           "contents": [
                                                                               {
                                                                                   "type": "text",
                                                                                   "text": "你的公司",
                                                                                   "weight": "bold"
                                                                               },
                                                                               {
                                                                                   "type": "text",
                                                                                   "text": "{}".format(
                                                                                       query.company_address),
                                                                                   "offsetTop": "10px"
                                                                               }
                                                                           ],
                                                                           "height": "130px"
                                                                       },
                                                                       "footer": {
                                                                           "type": "box",
                                                                           "layout": "vertical",
                                                                           "contents": [
                                                                               {
                                                                                   "type": "button",
                                                                                   "action": {
                                                                                       "type": "message",
                                                                                       "label": "點我編輯",
                                                                                       "text": "編輯公司"
                                                                                   }
                                                                               }
                                                                           ]
                                                                       }
                                                                   }
                                                               ]
                                                           }))


if __name__ == "__main__":
    app.run()
