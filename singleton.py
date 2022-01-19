"""
Singleton design pattern (Creational)
Ensure that a class has only one instance
Usage Example : Database connections, Hardware access, Config files
"""


class DBConnection:
    instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


if __name__ == '__main__':
    connection1 = DBConnection()
    connection2 = DBConnection()
    connection3 = DBConnection()

    print(id(connection1))
    print(id(connection2))
    print(id(connection3))

    print(id(connection1) == id(connection2) == id(connection3))
