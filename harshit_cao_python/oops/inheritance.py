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
    def __init__(self, brand, model_name, price, ram, internal_memory, real_camera):
        #two ways
        # Phone.__init__(self,brand,model_name, price) # uncommon way
        super().__init__(brand,model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.real_camera = real_camera

    def make_a_call(self, phone_number):
        print(f"calling {phone_number}......")

    def full_name(self):
        return f"{self.brand} {self.model_name}"


phone = Phone('nokia','1100',1000)
smartphone = SmartPhone('onePlue','Nord',30000,'8 GB','128 GB', '20 MP')
print(phone.full_name())
print(smartphone.full_name())
print(smartphone.full_name() + f" and price is {smartphone._price}")