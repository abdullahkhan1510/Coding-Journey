def main():
    student = get_student()
    if student [0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} is in {student[1]}")

def get_student():
    return input("Name: "), input("House: ")

if __name__ == "__main__":
    main()