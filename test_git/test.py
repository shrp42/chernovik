class Human:
    def __init__(self, name, last_name, age):
        self._name = name
        self._last_name = last_name
        self._age = age
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.last_name}\nВозраст: {self.age}"

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,new_name):
        if not isinstance(new_name,str):
            raise ValueError ("Имя должно быть строкой")
        self._name = new_name

    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self,new_last_name):
        if not isinstance(new_last_name,str):
            raise ValueError("Фамилия должна быть строкой")
        self._last_name = new_last_name

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,new_age):
        if not isinstance(new_age,int):
            raise ValueError("Возраст должен быть из цифр")
        self._age = new_age

def main():
    maga = Human("Maga", "Magomedov", 20)
    print(maga)

# проверка работы ошибки
    # try:
    #     maga.age = "двадцать"  # Пытаемся установить возраст строкой
    # except ValueError as e:
    #     print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
