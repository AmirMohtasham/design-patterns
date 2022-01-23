from observer.event_listeners import get_event_listeners


class EventProvider:
    events = None

    @classmethod
    def add_listener(cls, event_name, listener_obj):
        if cls.events is None:
            cls.events = {}

        if event_name not in cls.events:
            cls.events[event_name] = [listener_obj]
        else:
            cls.events[event_name].append(listener_obj)

    @classmethod
    def fire(cls, event_name, *args, **kwargs):
        if event_name in cls.events:
            for listener in cls.events[event_name]:
                listener().handle(*args, **kwargs)

    @classmethod
    def prepare_events(cls):
        event_listeners = get_event_listeners()
        for event in event_listeners.keys():
            for listener in event_listeners[event]:
                cls.add_listener(event, listener)
