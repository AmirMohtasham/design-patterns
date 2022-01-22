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
    3- Virtual Proxy(Lazy initialization)
"""

from abc import ABC, abstractmethod


class IPost(ABC):
    @abstractmethod
    def edit_post(self, new_title, new_content):
        pass


class Post(IPost):
    def __init__(self, title, content, user):
        self.title = title
        self.content = content
        self.user = user

    def edit_post(self, new_title, new_content):
        self.title = new_title
        self.content = new_content

    def __str__(self):
        return f"Post: {self.title}\n{self.content}"


class User:
    def __init__(self, name):
        self.name = name


class PostProxy(IPost):
    def __init__(self, post, user):
        self.post = post
        self.user = user

    def edit_post(self, new_title, new_content):
        if self.post.user == self.user:
            self.post.edit_post(new_title, new_content)
            return True
        print("Access Deny To Edit Post")
        return False


if __name__ == '__main__':
    user1 = User('Amir')
    user2 = User('Abbas')

    post1 = Post(title='post1', content='some text...', user=user1)
    print(post1)

    is_update = PostProxy(post1, user1).edit_post(new_title='post1-updated', new_content='this is test text ...')
    print(is_update)
    if is_update:
        print(post1)
