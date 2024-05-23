class Person:
    def __init__(self, Name, Age, Job):
        self.name = Name
        self.age = Age
        self.job = Job

    def introduction(self):
        print("")
        print(f" Hello Every one MY name is {self.name}")
        print(f"I am {self.age} years old")

    def Job(self):
        print(f"my Occupation is {self.job}")


Name = input("Enter you name : ")
Age = input("Enter your age : ")
Job = input("Enter you occupation : ")

a = Person("babe", 4, 3)
a.introduction()
a.Job()


print("")