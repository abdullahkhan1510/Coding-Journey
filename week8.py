class Wizard:
    def __init__(self,name):
        super().__init__(name)
        self.name = name

class Student(Wizard):
    def __Init__(self,name,house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = self.subject
wizard = Wizard("Albus")
student = Student("Harry","Gryffindor")
professor = Professor("Severus","Defense against the dark arts") 