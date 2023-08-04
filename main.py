class Rabbit:
    nr_of_rabbits = 0

    def __init__(self, age):
        self.age = age
        Rabbit.nr_of_rabbits += 1  # Intentionally wrong!


alice = Rabbit(2)
alice.nr_of_rabbits = 13
buddy = Rabbit(4)
charlie = Rabbit(7)
print(f"{alice.nr_of_rabbits = }")
print(f"{charlie.nr_of_rabbits = }")
