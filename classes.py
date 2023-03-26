## The most comprehensive class created
class Decorator():
    def __init__(self,name,description,price):
        self.name=name
        self.description=description
        self.price=price
    def get_name(self,name):
        self.name=name
        return f"Name of the product: {self.name}"
    def get_description(self,description):
        self.description=description
        return f"Description: {self.description}"     
    def get_cost(self,price):
        self.price=price
        return f"The amount you will pay: {self.price}"
   
## Created subclasses of Decorator class
class Shoes(Decorator):
    def __init__(self, name, description, price, gender,type):
        super().__init__(name, description, price)
        self.gender=gender
        self.type=type

class Watches(Decorator):
    def __init__(self, name, description, price, gender,type):
        super().__init__(name, description, price)
        self.gender=gender
        self.type=type

class Clothes(Decorator):
    def __init__(self, name, description, price, gender,type):
        super().__init__(name, description, price)
        self.gender=gender
        self.type=type

class Bags(Decorator):
    def __init__(self, name, description, price, gender,type):
        super().__init__(name, description, price)
        self.gender=gender
        self.type=type
