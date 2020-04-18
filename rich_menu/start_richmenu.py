import requests

def setRichmenu(richmenu_id):
    headers = {"Authorization":"Bearer 9gEcD6pNZWA9xe65jwSrzzykJnBNYhgBdqaUDpvafeMTyG0D+LELBnV/53HwYiue8bTWswthp0SjGEOzGy8UroCrCpfs2WWwbjGynTVFzJIjFYq2dAJZpDDXPqf5ki46kWvQbmmfCl9O58pb2QFFEQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

    req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/{richmenu_id}'.format(richmenu_id=richmenu_id),
                       headers=headers)

    print(req.text)