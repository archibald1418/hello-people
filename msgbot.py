import requests
import time

url = 'https://api.telegram.org/bot664546171:AAGj2JuquWDoV6cXD_WCY1Uh7rC0XzC27wk/'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0'}

def get_updates_json(request):
    params = {'timeout':100, 'offset':None}
    response = requests.get(request + 'getUpdates', data=params)
    time.sleep(1)
    return response.json()

def last_update(data):
    results = data['result']
    return results[-1]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat_id, text):
    params = {'chat_id':chat_id, 'text':text}
    response = requests.post(url + 'sendMessage', data=params)
    time.sleep(1)
    return response


if __name__ == '__main__':

    chat_id = get_chat_id(last_update(get_updates_json(url)))

    send_mess(chat_id, 'Your message goes here')

    print('Message sent')
