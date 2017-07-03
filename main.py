from animals import Animal, Dog, Dragon

animal1 = Animal('Generic Animal',100)
animal1.walk().walk().walk().run().run().display_health()

dog1 = Dog('Spot')
dog1.walk().walk().walk().run().run().pet().display_health()

dragon1 = Dragon('Trogdor')
dragon1.walk().walk().fly().display_health()

animal2 = Animal('New Animal')
# animal2.pet()
# animal2.fly()

dog2 = Dog('Bruno')
# dog2.fly()