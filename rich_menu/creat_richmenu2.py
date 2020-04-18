#菜單的
import requests
import json

headers = {"Authorization":"Bearer 9gEcD6pNZWA9xe65jwSrzzykJnBNYhgBdqaUDpvafeMTyG0D+LELBnV/53HwYiue8bTWswthp0SjGEOzGy8UroCrCpfs2WWwbjGynTVFzJIjFYq2dAJZpDDXPqf5ki46kWvQbmmfCl9O58pb2QFFEQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

body = {
    "size": {"width": 2500, "height": 1686},
    "selected": "true",
    "name": "Controller",
    "chatBarText": "Controller",
    "areas":[
        {
          "bounds": {"x": 0, "y": 0, "width": 833, "height": 843},
          "action": {"type": "postback", "label": "附近店家還沒開", "data":"附近店家"}
        },
        {
          "bounds": {"x": 833, "y": 0, "width": 833, "height": 843},
          "action": {"type": "postback", "label": "快速選單還沒做好", "data":"快速選單"}
        },
        {
          "bounds": {"x": 1686, "y": 0, "width": 833, "height": 843},
          "action": {"type": "postback", "label": "小幫手還在睡", "data":"小幫手"}
        },
        {
          "bounds": {"x": 0, "y": 843, "width": 833, "height": 843},
          "action": {"type": "postback", "label": "小幫手還在睡", "data":"搜尋"}
        },
        {
          "bounds": {"x": 833, "y": 843, "width": 833, "height": 843},
          "action": {"type": "postback", "label": "誰知道你老樣子", "data":"老樣子"}
        },
        {
          "bounds": {"x": 1686, "y": 843, "width": 833, "height": 843},
          "action": {"type": "postback", "label": "這是專屬於你的會員中心", "data":"會員中心"}
        }
    ]
  }

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)