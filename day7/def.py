class Student:
    name = ""
    roll = 0
    def __init__(self, x, y):
        self.name = x
        self.roll = y
    def display_info(self):
        print("name:" , self.name)
        print("roll:" , self.roll)
student1 =Student("jam", 100)
student1.name = "sam"
student1.roll = 101
student1.display_info()
student1.__init__("shiro", 102)
student1.display_info()
print(student1.name)
print(student1.roll)
    