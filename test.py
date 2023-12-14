class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def getData(self):
        print("name:", self._name, "age:", self._age)

s = Student("minji", 20)

class Exam:
    def __init__(self, subject):
        self._subject = subject
        self._score = score

    def getData(self):
        print("subject:", self._subject, "score:", self._score)
