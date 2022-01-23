from observer.providers.listener_provider import ListenerProvider


class SendSlackNotification(ListenerProvider):
    def handle(self, *args, **kwargs):
        print('Send slack notification ... ')
