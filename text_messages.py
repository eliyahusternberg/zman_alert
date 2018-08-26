import telesign
from telesign.messaging import MessagingClient
from shkia import get_shkia
import schedule
import time


def send_text(mobile_phone, msg):
    customer_id = "5822EFA3-0D31-4D97-A6B8-BB7A09F865FD"
    api_key = "ESqaCPvHsGh7V4513hFMf/+Y3BG1Zl/7Gt5irGhmfi/cMcI7DHwh2lIJwhyLMXThd54q6oWckRq5sZ/NeJo+zQ=="

    phone_number = mobile_phone
    message = msg
    message_type = "ARN"

    messaging = MessagingClient(customer_id, api_key)
    response = messaging.message(phone_number, message, message_type)
    print(response, messaging.message(phone_number, message, message_type))


schedule.every().saturday.do(send_text,input('Enter a phone number:'),'shkia is at {}'.format(get_shkia(input('Enter zipcode:'))))
while True:
    schedule.run_pending()
    time.sleep(1)
send_text(input('Enter your phone number:'), ('Shkia is at {}'.format(get_shkia(input('Enter zipcode')))))
