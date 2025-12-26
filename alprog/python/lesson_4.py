import time


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

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"

class Student(Person):
    def __init__(self, name:str, grade:int, lesson):
        super().__init__(name)
        self.grade = grade
        self.lesson = lesson

    def __str__(self):
        return f"Student: {self.name}, grade: {self.grade}, lesson: {self.lesson}"

# st1 = Student("Alice",5,"Math")
# print(st1)



#<2. Декораторы и генераторы>

