import random
class Hat:
    houses = ["Gryffindor","Hufflepuff","Slytherin","Ravenclaw"]
    @classmethod
    def sort(cls,name):
        house = random.choice(cls.houses)
        print(name, "is in", house)


hat = Hat()
hat.sort("Harry")