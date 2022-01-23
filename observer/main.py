"""
Observer Design Pattern (Behavioral)
(Listener Design Pattern)

Lets you define a subscription mechanism to notify multiple objects about
any events that happen to the object they’re observing.

Example:
    Suppose we have an app to register a user, and
     we want to send a message to Slack when the user registers and
     send a welcome email to the user and log the user data
"""

from observer.providers.event_provider import EventProvider

EventProvider.prepare_events()


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return self.email

    def register_user(self):
        print('registering user...')
        print(f'User registered successfully - {self.email} - {self.name}')
        EventProvider.fire('user_register', user=self)


if __name__ == '__main__':
    User("amirmohtasham.m@gmail.com", "Amir").register_user()
