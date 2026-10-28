class Student:
    def __init__(self):
        ...

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