
# class Laptop:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.name = brand+ ' ' +model

#     def apply_discount(self,num):
#         off_price = (num/100)*self.price
#         return self.price - off_price   



# l = Laptop('lenovo','ideapads-145', 46000)
# print(l.name)
# print(l.apply_discount)
# print(l.full_name)
 

# l = [1,2,3]
# list.append(l,10)
# print(l)


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


p1 = Person('Amol','Nagrale',30)
p2 = Person('Amit','Nagrale',32)
print(p1.first_name)
print(p2.last_name)
