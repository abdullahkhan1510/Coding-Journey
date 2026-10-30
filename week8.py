class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        if house not in["Hufflepuff", "Slytherin", "Ravenclaw", "Gryffindor"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
    #Getter
    def house(self):
        return self.house
    #Setter
    def house(self,house):
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} is in {student.house}")
def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name,house)
    return student
if __name__ == "__main__":
    main()