from observer.listeners.log_data import LogData
from observer.listeners.send_slack_notification import SendSlackNotification
from observer.listeners.send_welcome_email import SendWelcomeEmail


def get_event_listeners():
    return {
        'user_register': [
            SendWelcomeEmail,
            SendSlackNotification,
            LogData
        ]
    }
