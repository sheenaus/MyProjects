class Person:
    personcount = 0
    prof_type = ''
    def __init__(self, name, age,prof_type):
        self.name = name
        self.age = age
        self.prof_type=prof_type
        Person.personcount += 1
    def show_details(self):#public method
        print ("Name : ", self.name, ", Age: ", self.age, ", prof_type: " ,self.prof_type)
    def _protected_method(self):
        print("protected method")
    def __private_method(self):
        print("privated method")
class Employee(Person):
    def __init__(self, name, age,prof_type, dept,salary):
        super().__init__(name, age,prof_type)
        self.salary = salary
        self.dept=dept
    def show_details(self):
              # print("Name : ", self.name, ", Age: ", self.age, ", prof_type: ", self.prof_type)
               super().show_details()
               print( "Dept : ", self.dept, ", Salary: ", self.salary)

if __name__ == "__main__":
    p = Person("y", 23,"eng")
    x = Employee("x", 20, "eng","civil",100000)
    p.show_details() # Salary is unknown
    x.show_details() # Salary is 100000i
    p._protected_method() # shows a warning
    #p.__private_method()  #AttributeError: 'Person' object has no attribute '__private_method'