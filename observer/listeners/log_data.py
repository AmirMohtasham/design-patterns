from observer.providers.listener_provider import ListenerProvider


class LogData(ListenerProvider):
    def handle(self, *args, **kwargs):
        print(f"Log Data {kwargs['user']}...")
