class People:
    def __init__(self):
        self.list_ = []

    def show_list(self):
        for person in self.list_:
            print(person)
            print()

    def add_to_people(self, person):
    	self.list_.append(person)


class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def get_details(self):
        return f"Name: {self.name},\nAge:  {self.age},\nNationality: {self.nationality}\n"

    #  The __str__() function  is used to provide a readable
    #  and nice description of your object, mainly for end-users.

    def __str__(self):                     
        return self.get_details()

    
    #  The __repr__ function is used 
    #  To provide a precise and official string representation of the object,
    #  which is mainly for developers. Ideally, it should look like a valid 
    #  Python expression that could recreate the object.

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age}, nationality={self.nationality!r})"

    
    

p1 = Person("john", 18, "INDIAN")
p2 = Person("David", 22, "Nepal")
people = People()
people.add_to_people(p1)
people.add_to_people(p2)

# print(people.show_list()
# people.show_list()

print(p1)
print(str(p1))
print(repr(p1))
copy_p1 = eval(repr(p1))
print("\nCopy-P1 --> \n",copy_p1)
