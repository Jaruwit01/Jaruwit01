#--------การส้างคล้าสและออปเจ็ค
# class Book:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
        
#     def getdetalle(self):
#         print('Name: %s' % self.name)
#         print('Price: %d USD' % self.price)
        
# b1 = Book('Python Language', 59)
# b2 = Book('Java Language', 69)

# b1.getdetalle()
# b2.getdetalle()

# b1.price = 99
# b1.getdetalle()

# class Person:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
    
#     def getName(self):
#         return self.firstname + ' ' + self.lastname
    
# p = Person('Chase', 'Rice')
# p.career = 'Singer'
# p.country = 'USA'

# print('Name:' + p.getName())
# print('Career:' + p.career)
# print('Country:' + p.country)

# p2 = Person('Max', 'Graham')
# p2.genres = ['Electronica', 'trance', 'twch house', 'techno']

# print('Name: ' + p2.getName())
# print('Genres:', p2.genres)


# --------------Constructor และ Destructor
# class Person:
    
#     def __init__(self, firstName, lastName):
#         self.firstName = firstName
#         self.lastName = lastName
#         print('Object was created')
        
#     def getName(self):
#         return self.firstName + ' ' + self.lastName
    
#     def __del__(self):
#         print('Object was destoryed')
        
# p = Person('Cashe', 'Rice')
# print(p.getName())
# del p


#-------------Static variables และ Static methods

# from re import S

# from sympy import E


# class Box:
#     color = 'green'
    
#     def __init__(self, width, height, dept):
#         self.width = width
#         self.height = height
#         self.dept = dept
        
#     def getVolume(self):
#         return self.width * self.height * self.dept
    
#     @staticmethod
#     def compare(a, b):
#         if a.getVolume() > b.getVolume():
#             return 'greater than'
#         elif a.getVolume() == b.getVolume():
#             return 'equal'
#         else:
#             return 'less than'
        
# a = Box(2, 3, 4)
# b = Box(1, 2, 5)

# Box.color = 'red'

# print('Box a volume = %d' % a.getVolume())
# print('Box b volume = %d' % b.getVolume())
# print('Box a color = %s' % a.color)
# print('Box b color = %s' % b.color)

# print('Box a volum a is %s box b' % Box.compare(a, b))
        
        
from re import A


class Stro:
    def __init__(self, Name, Bq):
        self.Name = Name
        self.Bq = Bq
    
    def getStoke(self):
        print('Name: %s' % self.Name)
        print('Bq: %s' % self.Bq)

a,b = input().split()
c,d = input().split()
s = Stro(a, b)
s2 = Stro(c, d)

s.getStoke()
s2.getStoke()