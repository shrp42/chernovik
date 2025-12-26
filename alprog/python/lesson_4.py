import time
import random
import math

#<1. Классы и ООП>

class Car:
    def __init__(self, model):
        self.model = model

    def start(self):
        print(f"{self.model} заведен")

    def stop(self):
        print(f"{self.model} остановлен")

    def drive(self):
        print(f"{self.model} едет вперед")

class ElectricCar(Car):
    def __init__(self, model, charge):
        super().__init__(model)
        self.charge = charge

    def charge_battery(self):
        self.charge = 100
        print(f"{self.model} заряжен на {self.charge}%")

# BMW_I8 = ElectricCar("BMW I8", 50)
# BMW_I8.charge_battery()
# BMW_I8.start()
# BMW_I8.drive()
# BMW_I8.stop()

# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()      # время начала
#         result = func(*args, **kwargs)
#         end_time = time.time()        # время окончания
#         print(f"Function '{func.__name__}' executed in {end_time - start_time:.6f} seconds")
#         return result
#     return wrapper

class Person:

    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Student: {self.name}"

class Student(Person):

    # @timing_decorator
    def __init__(self, name:str, grade:int, lesson):
        super().__init__(name)
        self.grade = grade
        self.lesson = lesson
    def __str__(self):
        return f"Student: {self.name}, grade: {self.grade}, lesson: {self.lesson}"

# st1 = Student("Alice",5,"Math")
# print(st1)



#<2. Декораторы и генераторы>
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Function '{func.__name__}' was done in {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def timer():
    delay = time.sleep(2)
    print("kakashki")
# timer()



def fen_nums():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for num in fen_nums():
    if num > 150:
        break
    # print(num, end=" ")



#<3. Работа с модулями>
random_list = [random.randint(1,100) for _ in range(12)]
sorted_list = sorted(random_list)
reverse_sorted_list = sorted(random_list, reverse = True)
# print(f"Sorted random list: {sorted_list}\n"
#       f"Reverse sorted random list: {reverse_sorted_list}")



def math_operations():
    x = int(input("Enter your number: "))
    fact = math.factorial(x) if x >= 0 else "undefined"
    sqrt = math.sqrt(x) if x >= 0 else "undefined"
    power = math.pow(x, 2)
    print(f"Number {x}: \n"
          f"Factorial: {fact}\n"
          f"Square root: {sqrt}\n"
          f"Squared (x^2): {power}")

# math_operations()



# 1. Список квадратов чисел от 1 до 20
squares = [x**2 for x in range(1, 21)]
# print("Список квадратов:", squares)

# 2. Удвоение всех чисел
doubled = list(map(lambda x: x*2, squares))
# print("Удвоенные числа:", doubled)

# 3. Отбор чисел, делящихся на 3
div_by_3 = list(filter(lambda x: x % 3 == 0, doubled))
# print("Числа, делящиеся на 3:", div_by_3)