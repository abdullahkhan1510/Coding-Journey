class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name,house)
def main():
    student = Student.get()
    print(f"{student.name} is in {student.house}")

if __name__ == "__main__":
    main()