class Animal(object):
    def __init__(self, name, health=100):
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
        print "{}'s health: {}".format(self.name, self.health)


class Dog(Animal):
    def __init__(self, name, health=150):
        super(Dog, self).__init__(name, health)

    def pet(self):
        self.health += 5
        return self


class Dragon(Animal):
    def __init__(self, name, health=170):
        super(Dragon, self).__init__(name, health)

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon, self).display_health()
        print 'I am a Dragon'