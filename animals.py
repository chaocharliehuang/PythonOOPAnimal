class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        self.update_health()
        return self
    
    def run(self):
        self.health -= 5
        self.update_health()
        return self

    def update_health(self):
        if self.health < 0:
            self.health = 0
        return self

    def display_health(self):
        print "Health:", self.health


class Dog(Animal):
    super(Dog, self).__init__()
    