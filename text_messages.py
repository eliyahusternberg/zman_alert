import telesign
from telesign.messaging import MessagingClient
import shkia


def send_text(mobil_phone,msg):
    def send_text_to_user(html: object, alert: object):
        customer_id = "5822EFA3-0D31-4D97-A6B8-BB7A09F865FD"
        api_key = "ESqaCPvHsGh7V4513hFMf/+Y3BG1Zl/7Gt5irGhmfi/cMcI7DHwh2lIJwhyLMXThd54q6oWckRq5sZ/NeJo+zQ=="

        phone_number = "15163128958"
        message = "Shkia is at..."
        message_type = "ARN"

        messaging = MessagingClient(customer_id, api_key)
        response = messaging.message(phone_number, message, message_type)
        print(response, messaging.message(phone_number, message, message_type))
