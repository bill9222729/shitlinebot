from line_bot_api import *
import datetime

def record_message_event(event):
    Received_time = datetime.datetime.fromtimestamp(int(event.timestamp / 1000))
    Received_message = event.message.text
    user_name = line_bot_api.get_profile(event.source.user_id).display_name
    file_path = 'history//{user_name}.txt'.format(user_name=user_name)
    f = open(file_path, 'a')
    f.write(str(Received_time) + '  ' + Received_message + '\n')
    print(str(Received_time) + '  ' + Received_message + '\n')