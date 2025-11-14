class Person:
    def __init__(self,name):
        self.name=name
    def call_person(self,other_person):
        print(f"{self.name} is calling {other_person}")

print(Person)
ali = Person('Ali')
ali.call_person("Reza")
print(ali.name)
person_2 = ali
person_2.name = 'aaa'
ali.name = 'pppp'
print(person_2.name)