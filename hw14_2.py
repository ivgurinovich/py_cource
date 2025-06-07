from idlelib.pyshell import extended_linecache_checkcache


class BeePhant:
    def __init__(self, bee, elephant):
        self.bee = max(0,min(100, bee))
        self.elephant = max(0,min(100, elephant))

    def fly(self):
        return self.bee >= self.elephant

    def trumpet(self):
        if self.elephant >= self.bee:
            return 'tu-tu-doo-doo'
        else:
            return 'wzzzz'

    def eat(self, meal, value):
        if meal == 'nectar':
            self.bee = min(100, self.bee + value)
            self.elephant = max(0, self.bee - value)
        elif meal == 'grass':
            self.bee = max(0, self.bee + value)
            self.elephant = min(100, self.bee - value)
        else:
            raise ValueError('meal is nectar or grass')


ps = BeePhant(40,50)
print(f"fly  = {ps.bee}, elephant = {ps.elephant}")
print(ps.fly())
print(ps.trumpet())
ps.eat('grass', 40)
print(f"fly  = {ps.bee}, elephant = {ps.elephant}")
print(ps.fly())
print(ps.trumpet())