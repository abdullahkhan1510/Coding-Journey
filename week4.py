import random

def main():
    entered = get_level()
    for i in range(0,10):
        x = generate_integer(entered)
        y = generate_integer(entered)
        for j in range(0,3):
            user_answer = int(input(f"{x} + {y} = "))
            sum = x+y
            if user_answer == sum:
                break
            elif j  == 2:
                print(f"{x} + {y} = {sum}")
                break
            elif user_answer != sum:
                print("EEE")



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1 and level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
