from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('9gEcD6pNZWA9xe65jwSrzzykJnBNYhgBdqaUDpvafeMTyG0D+LELBnV/53HwYiue8bTWswthp0SjGEOzGy8UroCrCpfs2WWwbjGynTVFzJIjFYq2dAJZpDDXPqf5ki46kWvQbmmfCl9O58pb2QFFEQdB04t89/1O/w1cDnyilFU=')

with open("G:\\Users\\蕭光佑\\PycharmProjects\\lineBot\\venv\\image\\rich_menu01.jpeg",'rb') as f:
    print(f)
    line_bot_api.set_rich_menu_image("richmenu-2d42e0875790d72573a316b7a214bded", "image/jpeg", f)