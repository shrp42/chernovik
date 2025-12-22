#<1. Файлы>
nums = [1, 2, 3, 4, 5,6,7,8,9]

# запись в файл
with open("file_nums.txt", "w") as file:
    for n in nums:
        file.write(str(n) + "\n")

# чтение из файла
with open("file_nums.txt", "r") as file:
    nums_from_file = [int(line.strip()) for line in file]

# print(nums_from_file)



with open("text.txt", "r") as text_file:
    lines = text_file.readlines()

nums_lines = len(lines)
nums_words = sum(len(line.split()) for line in lines)

# print(f"Количество слов в файле text.txt: {nums_words}")
# print(f"Количество строчек в файле text.txt: {nums_lines}")





#<2. Исключения>
def num():
    while True:
       try:
          n = int(input("Enter your number:"))
          print(f"Your number is {n}")
          break
       except ValueError :
           print('Print number')

# num()



def z_error():
    while True:
        try:
          a = int(input("Enter first number:"))
          b = int(input("Enter second number:"))
          c = a / b
        except ZeroDivisionError :
            print("You cant divide by zero")
            continue
        except ValueError:
            print("Enter number")
            continue
        else:
            print(f"Your result is {c}")
            break

z_error()