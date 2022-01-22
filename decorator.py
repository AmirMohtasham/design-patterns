"""
Decorator Design Pattern (Structural)

Allows you to change the behavior of an object dynamically at runtime by the decorator class.
This pattern uses a combination instead of inheritance.
Decorator pattern makes it possible to add behavior to an object dynamically without changing
the behavior of other objects in the same class.

"""

TAX_RATE = {
    'USA': 23,
    'UAE': 10
}


class Product:
    def __init__(self, name, price, address):
        self.name = name
        self.price = price
        self.address = address

    def get_price(self):
        return self.price


class Address:
    def __init__(self, country, detail):
        self.country = country
        self.detail = detail


class ProductDecorator:
    def __init__(self, product_object):
        self.product_object = product_object  # combination

    def get_price(self):
        country = self.product_object.address.country
        return self.product_object.get_price() * (1 + TAX_RATE[country])


if __name__ == '__main__':
    address_usa = Address('USA', 'some details...')
    address_uae = Address('UAE', 'some details...')

    p1 = Product(name='Galaxy 780', price=2000, address=address_usa)
    p2 = Product(name='Galaxy ZSlide', price=3000, address=address_uae)

    print(f"Product1 => Price without tax: {p1.get_price()}")
    print(f"Product2 => Price without tax: {p2.get_price()}")

    product1_decorator = ProductDecorator(p1)
    print(f"Product1 => Price with tax: {product1_decorator.get_price()}")

    product2_decorator = ProductDecorator(p2)
    print(f"Product2 => Price with tax: {product2_decorator.get_price()}")
