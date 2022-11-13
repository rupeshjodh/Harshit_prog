#polymorphism



class Rabbit():
    def age(self):
        print("This function determines the age of Rabbit.")

    def color(self):
        print("This function determines the color of Rabbit.")


class Horse():
    def age(self):
        print("This function determines the age of Horse.")

    def color(self):
        print("This function determines the color of Horse.")


obj1 = Rabbit()
obj2 = Horse()
for type in (obj1, obj2):  # creating a loop to iterate through the obj1, obj2
    type.age()
    type.color()