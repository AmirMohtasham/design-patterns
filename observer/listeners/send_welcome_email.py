from observer.providers.listener_provider import ListenerProvider


class SendWelcomeEmail(ListenerProvider):
    def handle(self, *args, **kwargs):
        print('Send email ...')
