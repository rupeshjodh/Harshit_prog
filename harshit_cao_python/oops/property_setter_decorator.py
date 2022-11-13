# will discuss three problems in existing
# then we will solve them using getter, setter decorator

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)
        # if price > 0 :
        #     self.price = price
        # else:
        #     self.price = 0

        # self.complate_specification = f"{self.brand} {self.model_name} and price is {self.price} of phone"

    @property # it treated as a class attribute
    def complate_specification(self):
        return f"{self.brand} {self.model_name} and price is {self._price} of phone"
    
    @property # getter
    def price(self):
        return self._price

    @price.setter #setter
    def price(self,new_price):
        self._price = max(new_price,0) 


    def make_a_call(self, phone_number):
        print(f"calling {phone_number}......")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

phone1 = Phone('Nokia','1100',1000)
print(phone1.brand)
print(phone1.model_name)
print(phone1._price)
phone1.price = -500
# print(phone1.complate_specification())
print(phone1.complate_specification)
