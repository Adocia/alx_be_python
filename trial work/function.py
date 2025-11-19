def greet(name):
    print(f"Hello, {name}!")
greet("Francia")


def favorite_food(food):
    print(f"My favorite food is {food}")
favorite_food("fufu and soup")

add = lambda x, y: x + y
result = add(5, 3)
print(result)

def calculate_area(length, width):
    area = length * width
    return area
calculate_area(10, 5)

def user_info(name, age=None):
    print(f"Name: {name}")
    if age:
        print(f"Age: {age}")
user_info("Bob", age = 30)


def greet(name = "World"):
    print(f"Hello!, {name}!")
greet()

greet("Alice")

greet("Ama")


def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

    check_even_odd(20)
    
    check_even_odd(15)
