class Student:
    def __init__(self,name,house,patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in["Hufflepuff", "Slytherin", "Ravenclaw", "Gryffindor"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell Terrier":
                return "🐕"
            case _:
                return "🪄"

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())
def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    student = Student(name,house,patronus)
    return student
if __name__ == "__main__":
    main()