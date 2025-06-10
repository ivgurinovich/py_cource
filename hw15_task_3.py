class Pizza:
    def __init__(self, size=None, cheese=False, pepperoni=False, mushrooms=False, onions=False, bacon=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        topping = []
        if self.cheese: topping.append('cheese')
        if self.pepperoni: topping.append('pepperoni')
        if self.mushrooms: topping.append('mushrooms')
        if self.onions: topping.append('onions')
        if self.bacon: topping.append('bacon')
        return f"Pizza size: {self.size}\nIngredients: {', '.join(topping)}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def pick_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_onions(self):
        self.pizza.onions = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def build(self):
        return self.pizza


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def make_small_pizza(self):
        self.builder.pick_size("Small")
        self.builder.add_cheese()
        self.builder.add_pepperoni()
        self.builder.add_mushrooms()
        self.builder.add_onions()
        self.builder.add_bacon()
        self.builder.build()
        return self.builder.pizza

    def make_large_pizza(self):
        self.builder.pick_size("Large")
        self.builder.add_cheese()
        self.builder.add_pepperoni()
        self.builder.add_mushrooms()
        self.builder.add_onions()
        self.builder.add_bacon()
        self.builder.build()
        return self.builder.pizza


builder = PizzaBuilder()
director = PizzaDirector(builder)

pizza1 = director.make_small_pizza()
print(pizza1)

pizza2 = director.make_large_pizza()
print(pizza2)
