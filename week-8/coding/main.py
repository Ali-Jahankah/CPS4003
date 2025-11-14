class Person:
    def __init__(self):
        self.name=None
    def call_person(self,other_person):
        print(f"{self.name} is calling {other_person}")


ali = Person()
ali.name="Ali"
ali.call_person("Reza")
print(ali.name)
person_2 = ali
person_2.name = 'aaa'
ali.name = 'pppp'
print(person_2.name)