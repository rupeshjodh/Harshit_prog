# can we derive more than one class from base class?
# multiple inheritance
# method resolution order
# method overriding
# isinstance(), issubclass()

class Phone: # base class/ parent class
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

    def make_a_call(self, phone_number):
        print(f"calling {phone_number}......")

    def full_name(self):
        return f"{self.brand} {self.model_name}"


class SmartPhone(Phone): # derived class/ child class
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        #two ways
        # Phone.__init__(self,brand,model_name, price) # uncommon way
        super().__init__(brand,model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera


    def full_name(self):  # method overriding
        return f"{self.brand} {self.model_name} and ram is {self.ram} "

class FlagShipPhone(SmartPhone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand, model_name, price, ram, internal_memory, rear_camera)
        self.front_camera = front_camera

    def full_name(self): # method overriding
        return f"{self.brand} {self.model_name} and ram is {self.ram} and front camera is {self.front_camera} "

# phone = Phone('nokia','1100',1000)
smartphone7 = SmartPhone('onePlue','Nord',30000,'8 GB','128 GB', '20 MP')
oneplus = FlagShipPhone('onePlue','Nord',30000,'8 GB','128 GB', '20 MP','18 MB')
# print(phone.full_name())
# print(smartphone.full_name())
# print(smartphone.full_name() + f" and price is {smartphone._price}")
print(oneplus.full_name() + f" and price is {oneplus._price}")
# print(help(Phone)) # MRO
# print(help(SmartPhone)) #MRO
# print(oneplus.full_name)
# print(help(FlagShipPhone)) #MRO
# print(isinstance(smartphone7, SmartPhone)) # True
# print(isinstance(oneplus, FlagShipPhone))# True
# print(isinstance(oneplus, Phone))# True

print(issubclass(FlagShipPhone, SmartPhone)) # True
print(issubclass(FlagShipPhone, Phone)) # True
print(issubclass(Phone, FlagShipPhone)) # False 