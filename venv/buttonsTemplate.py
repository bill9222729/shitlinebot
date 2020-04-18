import line_bot_api
import  datetime

def ButtonsTemplate_send_message(user_id):
    # 這是一個傳送按鈕的模板，架構解說
    buttons_template_message = line_bot_api.TemplateSendMessage(
        alt_text = '我是按鈕模板',  # 當你發送到你的Line bot 群組的時候，通知的名稱
        template = line_bot_api.ButtonsTemplate(
            thumbnail_image_url = 'http://shareboxnow.com/wp-content/uploads/2020/02/th.jpeg',  # 你的按鈕模板的圖片是什麼
            title = 'M&M Share',  # 你的標題名稱
            text = '請選擇你要的項目：',  # 應該算是一個副標題
            # 下面主要就是你希望使用者點擊了按鈕會有哪些動作，最多只能有四個action！超過會報錯喔！
            actions = [
                # 說真的這個我不知道要幹嘛用，可能後台可以收數據？我點了就回應我 postback text，至於data我就不熟了
                line_bot_api.PostbackAction(
                    label = 'postback',  # 在按鈕模板上顯示的名稱
                    display_text = 'postback text',  # 點擊會顯示的文字
                    data = 'action=buy&itemid=1'  # 這個...我真的就不知道了～
                ),
                # 跟上面差不多
                line_bot_api.MessageAction(
                    label = '現在幾點了？',   # 在按鈕模板上顯示的名稱
                    text = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 點擊後，顯示現在的時間，這些都可以隨意修改喔！
                ),
                # 跳轉到URL
                line_bot_api.URIAction(
                    label = '我的部落格',  # 在按鈕模板上顯示的名稱
                    uri = 'http://shareboxnow.com/'  # 跳轉到的url，看你要改什麼都行，只要是url
                ),
                # 這裡可以跟上面一樣，可以重複不限定只有一個 URIAction
                line_bot_api.URIAction(
                    label = 'Google',  # 在按鈕模板上顯示的名稱
                    uri = 'https://www.google.com.tw/'  # 跳轉到的url，看你要改什麼都行，只要是url
                )
            ]
        )
    )
    line_bot_api.line_bot_api.push_message(user_id, line_bot_api.TemplateSendMessage(buttons_template_message))