# class veriable
# circle
# area
# circumferance
# class Circle:
#     pi = 3.14
#     def __init__(self,radius):
#         self.radius = radius
#     def calc_circumferance(self):
#         return 2*Circle.pi*self.radius


# c = Circle(4)
# c1 = Circle(5)
# print(c.calc_circumferance())

# practice

class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    def calc_circumferance(self):
        return 2*Circle.pi*self.radius
        
c = Circle(4)
print(c.calc_circumferance())


#========================================================

class Laptop:
    discount_percent = 10
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.name = brand+ ' ' +model

    def apply_discount(self):
        off_price = (self.discount_percent/100)*self.price
        return self.price - off_price 
          
# self variable used when we want variable object
# class name when we want same object

# Laptop.discount_percent = 20
l1 = Laptop('lenovo','ideapads-145', 46000)
l2 = Laptop('apple','macbook-pro', 80000)
l2.discount_percent = 50
print(l2.__dict__)
# print(l1.apply_discount())
print(l2.apply_discount())
# print(l1.__dict__)
# print(l2.__dict__)
 

 