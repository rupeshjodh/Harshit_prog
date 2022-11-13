# In this video we will talk about
# Encapsulation # wrapping important variables & methods in single unit
# Abstraction # for hiding the complecity, without encapsulation abstraction is not possible
# Some special naming convention
# Name Mangling # __name (not a naming convection)


class Phone:
    def __init__(self, brand, model_name, __price):
        self.brand = brand
        self.model_name = model_name
        self.__price = __price

    def make_a_call(self, phone_number):
        print(f"calling {phone_number} ........")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_message(self):
        pass

phone1 = Phone('nokia','1100',1000)
print(phone1.__price)
print(phone1._Phone__price)

l = [3,2,4,1] 
l.sort() # tim sort
print(l)

#_name # convention of private name
# __name__ # dunder method