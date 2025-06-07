class Product:
    def __init__(self, name, store, price):
        self.__name = name
        self.__price = price
        self.__store = store

    def get_name(self):
        return self.__name

    def get_store(self):
        return self.__store

    def get_price(self):
        return self.__price

    def get_info(self):
        return f"{self.__name} from {self.__store}, price: {self.__price}"

    def __add__(self, other):
        return self.__price + other.get_price()


class Warehouse:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_by_index(self, index):
        if 0 <= index < len(self.__products):
            print(self.__products[index].get_info())
        else:
            print("Wrong index")

    def search_by_name(self, name):
        found = False
        for product in self.__products:
            if product.get_name().lower() == name.lower():
                print(product.get_info())
                found = True
        if not found:
            print("Product not found")

    def sort_by_name(self):
        self.__products.sort(key=lambda p: p.get_name())

    def sort_by_store(self):
        self.__products.sort(key=lambda p: p.get_store())

    def sort_by_price(self):
        self.__products.sort(key=lambda p: p.get_price())

    def show_all(self):
        for product in self.__products:
            print(product.get_info())


product1 = Product("Milk", "Walmart", 3.99)
product2 = Product("Bread", "Costco", 2.00)
product3 = Product("Cheese", "Rublevskiy", 5.00)

wh = Warehouse()
wh.add_product(product1)
wh.add_product(product2)
wh.add_product(product3)

wh.sort_by_name()
wh.show_all()
