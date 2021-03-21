from socket import *
import time
import argparse

from common.utils import send_message, get_data_from_message

def presence(s):
    msg_presence = { # Формируем presence-сообщение
        "action": "presence",
        "time": int(time.time()),
        "type": "status",
        "user": {
            "account_name": "Helik",
            "status": "connect"
        }
    }

    send_message(s, msg_presence) # переходим в фукнцию и отправляем сообщение с параметрами

    data = get_data_from_message(s.recv(1000000))
    print('Сообщение от сервера: ', data)

s = socket(AF_INET, SOCK_STREAM) # sockect - Создаём сокет TCP
s.connect(('localhost', 7777)) # .connect -  Устанавливаем соедение с сервером

presence(s) # переходим в функцию для отправки presence-сообщениz

s.close() # .close - Закрыть соединение
