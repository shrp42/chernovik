class Teacher:
      def __init__(self, name, subject):
          self.name = name
          self.subject = subject
 
      def teach(self):
          print(f"{self.name} is teaching {self.subject}.")

def main():
    teacher = Teacher("Mr. Smith", "Mathematics")
    teacher.teach()

print('sosal')