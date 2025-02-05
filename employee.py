class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def display(self):
        print(self.name)
        print(self.id)

class employee(Person):
    def __init__(self, name, id, post, salary):
        self.post = post
        self.salary = salary
        
        Person.__init__(self,name, id)
        
        
a= employee("Alexis", 907625, "intern", 0)

a.display()