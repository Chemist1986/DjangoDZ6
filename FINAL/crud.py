from .models import Client, Product, Order

# Создание нового клиента
def create_client(name, email, phone_number, address):
    client = Client(name=name, email=email, phone_number=phone_number, address=address)
    client.save()
    return client

# Создание нового товара
def create_product(name, description, price, quantity):
    product = Product(name=name, description=description, price=price, quantity=quantity)
    product.save()
    return product

# Создание нового заказа
def create_order(client, products, total_amount):
    order = Order(client=client, total_amount=total_amount)
    order.save()
    order.products.add(*products)
    return order