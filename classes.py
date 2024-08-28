class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Sajin", 21)

print(p1)

# - <__main__.Person object at 0x000002150F4B40D0>

print(p1.name)
print(p1.age)

'''
O/P

Sajin
21
'''