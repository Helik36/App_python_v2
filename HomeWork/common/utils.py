import json

def get_data_from_message(response):
    response_str = response.decode('utf-8') # идёт расшифровка сообщения переданная от клиента, переданная от server
    return json.loads(response_str)

def send_message(s, msg_response): # принимаем параметры отправленные от клиента
    msg = json.dumps(msg_response)
    s.send(bytes(msg, encoding="utf-8")) # отправялем сообщение