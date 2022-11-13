# class Person:
#     pass


# p1 = Person()
# print(Person.count_instance)

class Person:
    count_instance = 0
    def __init__(self, first_name, last_name, age):
        Person.count_instance +=1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('Amol','Nagrale',24)
p2 = Person('Amit','Nagrale',24)
p3 = Person('Amita','Nagrale',24)
print(Person.count_instance)
    


# class Laptop:
#     def __init__(self, brand, name,price):
#         self.brand = brand
#         self.name = name
#         self.price = price
#         self.laptop_name = brand+" "+name

#     def apply_discount(self,num):
#         off_price = (num/100)*self.price
#         return self.price - off_price

# laptop1 = Laptop('hp','adsjk324',65000)
# # print(laptop1.name)
# # print(laptop1.laptop_name)
# print(laptop1.apply_discount(50))



