from socket import *
import time

from common.utils import send_message, get_data_from_message

def send_answer(client):
    msg_response = {
        "response": '200',
        'time': int(time.time())
    }
    send_message(client, msg_response)


s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind(('', 7777))                # Присваивает порт 777
s.listen(5)                       # Переходит в режим ожидания запросов;

while True:
    client, addr = s.accept() # принять установку на соединение
    data_client = get_data_from_message(client.recv(1000000)) # Идёт обращение в Json файл, где идёт расшифровка сообщения от клиента
    print('Сообщение: ', data_client, ', было отправлено клиентом: ', addr)

    send_answer(client)

    client.close()
