"""
Proxy Design Pattern (Structural)
Proxy mean's mediator.

Proxy design pattern is the use of an intermediary to prevent direct access to
the main object and centralize access control.

In a way that we want to solve the challenges of accessing the program objects and
at the same time not change the interface of the main class.

To put it simply:
    We can restrict access to an object without changing its class

*Use cases:
    1- Protection Proxy
    2- Logging Proxy
    3- Virtual Proxy(Lazy initialization) (below example is for this item)

Lazy initialization : create instance of class if we need it
"""

from time import sleep


class MysqlConnector:
    def __init__(self):
        sleep(5)

    def connect(self):
        print('connect to mysql')


class MongoConnector:
    def __init__(self):
        sleep(1)

    def connect(self):
        print('connect to mongo')


class RedisConnector:
    def __init__(self):
        sleep(1)

    def connect(self):
        print('connect to redis')


class LazyLoader:
    def __init__(self, cls):
        self.cls = cls
        self.object = None

    def __getattr__(self, item):
        if self.object is None:
            self.object = self.cls()
        return getattr(self.object, item)


if __name__ == '__main__':
    mysql = LazyLoader(MysqlConnector)
    # mysql.connect()

    mongo = LazyLoader(MongoConnector)
    mongo.connect()

    redis = LazyLoader(RedisConnector)
    redis.connect()

    print('all databases connected')
