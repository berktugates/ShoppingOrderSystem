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

## Derived objects for item titles to sell

# Men's shoes objects
men_shoes1=Shoes("Sneakers 1","These sneakers are very high quality and sturdy.","200€","Men","Sneakers")
men_shoes2=Shoes("Sneakers 2","These sneakers are very high quality and sturdy.","220€","Men","Sneakers")
men_shoes3=Shoes("Sneakers 3","These sneakers are very high quality and sturdy.","180€","Men","Sneakers")
men_shoes4=Shoes("Casual 1","These casual shoes are very high quality and sturdy.","80€","Men","Casual Shoes")
men_shoes5=Shoes("Casual 2","These casual shoes are very high quality and sturdy.","90€","Men","Casual Shoes")
men_shoes6=Shoes("Casual 3","These casual shoes are very high quality and sturdy.","70€","Men","Casual Shoes")
men_shoes7=Shoes("Walking 1","These walking shoes are very high quality and sturdy.","120€","Men","Walking Shoes")
men_shoes8=Shoes("Walking 2","These walking shoes are very high quality and sturdy.","140€","Men","Walking Shoes")
men_shoes9=Shoes("Walking 3","These walking shoes are very high quality and sturdy.","170€","Men","Walking Shoes")
men_shoes10=Shoes("Spikes 1","These spikes are very high quality and sturdy.","370€","Men","Spikes")
men_shoes11=Shoes("Spikes 2","These spikes are very high quality and sturdy.","420€","Men","Spikes")
men_shoes12=Shoes("Spikes 3","These spikes are very high quality and sturdy.","250€","Men","Spikes")
men_shoes13=Shoes("Boots 1","These boots are very high quality and sturdy.","50€","Men","Boots")
men_shoes14=Shoes("Boots 2","These boots are very high quality and sturdy.","140€","Men","Boots")
men_shoes15=Shoes("Boots 3","These boots are very high quality and sturdy.","90€","Men","Boots")

# Women's shoes objects
women_shoes1=Shoes("Sneakers 1","These sneakers are very high quality and sturdy.","200€","Women","Sneakers")
women_shoes2=Shoes("Sneakers 2","These sneakers are very high quality and sturdy.","220€","Women","Sneakers")
women_shoes3=Shoes("Sneakers 3","These sneakers are very high quality and sturdy.","180€","Women","Sneakers")
women_shoes4=Shoes("Casual 1","These casual shoes are very high quality and sturdy.","80€","Women","Casual Shoes")
women_shoes5=Shoes("Casual 2","These casual shoes are very high quality and sturdy.","90€","Women","Casual Shoes")
women_shoes6=Shoes("Casual 3","These casual shoes are very high quality and sturdy.","70€","Women","Casual Shoes")
women_shoes7=Shoes("Heeled 1","These heeled shoes are very high quality,elegant and stylish","120€","Women","Heeled Shoes")
women_shoes8=Shoes("Heeled 2","These heeled shoes are very high quality,elegant and stylish","140€","Women","Heeled Shoes")
women_shoes9=Shoes("Heeled 3","These heeled shoes are very high quality,elegant and stylish","170€","Women","Heeled Shoes")
women_shoes10=Shoes("Flat 1","These flat shoes are very high quality and sturdy.","370€","Women","Flat Shoes")
women_shoes11=Shoes("Flat 2","These flat shoes are very high quality and sturdy.","420€","Women","Flat Shoes")
women_shoes12=Shoes("Flat 3","These flat shoes are very high quality and sturdy.","250€","Women","Flat Shoes")
women_shoes13=Shoes("Boots 1","These boots are very high quality and sturdy.","50€","Women","Boots")
women_shoes14=Shoes("Boots 2","These boots are very high quality and sturdy.","140€","Women","Boots")
women_shoes15=Shoes("Boots 3","These boots are very high quality and sturdy.","90€","Women","Boots")

# Men watch objects
men_watches1=Watches("Digital 1","Our latest waterproof digital watch model","750€","Men","Digital")
men_watches2=Watches("Digital 2","Our latest waterproof digital watch model","820€","Men","Digital")
men_watches3=Watches("Digital 3","Our latest waterproof digital watch model","640€","Men","Digital")
men_watches4=Watches("Classic 1","Our latest model, stylish, elegant and magnificent classic watch model","350€","Men","Classic")
men_watches5=Watches("Classic 2","Our latest model, stylish, elegant and magnificent classic watch model","1000€","Men","Classic")
men_watches6=Watches("Classic 3","Our latest model, stylish, elegant and magnificent classic watch model","540€","Men","Classic")
men_watches7=Watches("Sports 1","Our latest model, stylish, elegant and magnificent sports watch model","540€","Men","Sports")
men_watches8=Watches("Sports 2","Our latest model, stylish, elegant and magnificent sports watch model","540€","Men","Sports")
men_watches9=Watches("Sports 3","Our latest model, stylish, elegant and magnificent sports watch model","540€","Men","Sports")

# Women watch objects
women_watches1=Watches("Digital 1","Our latest waterproof digital watch model","820€","Women","Digital")
women_watches2=Watches("Digital 2","Our latest waterproof digital watch model","750€","Women","Digital")
women_watches3=Watches("Digital 3","Our latest waterproof digital watch model","640€","Women","Digital")
women_watches4=Watches("Classic 1","Our latest model, stylish, elegant and magnificent classic watch model","350€","Women","Classic")
women_watches5=Watches("Classic 2","Our latest model, stylish, elegant and magnificent classic watch model","1000€","Women","Classic")
women_watches6=Watches("Classic 3","Our latest model, stylish, elegant and magnificent classic watch model","540€","Women","Classic")
women_watches7=Watches("Sports 1","Our latest model, stylish, elegant and magnificent sports watch model","540€","Women","Sports")
women_watches8=Watches("Sports 2","Our latest model, stylish, elegant and magnificent sports watch model","540€","Women","Sports")
women_watches9=Watches("Sports 3","Our latest model, stylish, elegant and magnificent sports watch model","540€","Women","Sports")

# Men's clothing objects
men_clothes1=Clothes("T-Shirt 1","One of our newest style t-shirts","20€","Men","T-Shirt")
men_clothes2=Clothes("T-Shirt 2","One of our newest style t-shirts","24€","Men","T-Shirt")
men_clothes3=Clothes("T-Shirt 3","One of our newest style t-shirts","10€","Men","T-Shirt")
men_clothes4=Clothes("Sweatshirt 1","One of our newest style sweatshirts","25€","Men","Sweatshirt")
men_clothes5=Clothes("Sweatshirt 2","One of our newest style sweatshirts","47€","Men","Sweatshirt")
men_clothes6=Clothes("Sweatshirt 3","One of our newest style sweatshirts","56€","Men","Sweatshirt")
men_clothes7=Clothes("Shirt 1","One of our newest style shirts","22€","Men","Shirt")
men_clothes8=Clothes("Shirt 2","One of our newest style shirts","28€","Men","Shirt")
men_clothes9=Clothes("Shirt 3","One of our newest style shirts","36€","Men","Shirt")
men_clothes10=Clothes("Fleece 1","One of our newest style fleece","48€","Men","Fleece")
men_clothes11=Clothes("Fleece 2","One of our newest style fleece","66€","Men","Fleece")
men_clothes12=Clothes("Fleece 3","One of our newest style fleece","45€","Men","Fleece")

# Women's clothing objects
women_clothes1=Clothes("T-Shirt 1","One of our newest style t-shirts","20€","Women","T-Shirt")
women_clothes2=Clothes("T-Shirt 2","One of our newest style t-shirts","24€","Women","T-Shirt")
women_clothes3=Clothes("T-Shirt 3","One of our newest style t-shirts","10€","Women","T-Shirt")
women_clothes4=Clothes("Crop 1","One of our newest style crop","25€","Women","Crop")
women_clothes5=Clothes("Crop 2","One of our newest style crop","47€","Women","Crop")
women_clothes6=Clothes("Crop 3","One of our newest style crop","56€","Women","Crop")
women_clothes7=Clothes("Shirt 1","One of our newest style shirts","22€","Women","Shirt")
women_clothes8=Clothes("Shirt 2","One of our newest style shirts","28€","Women","Shirt")
women_clothes9=Clothes("Shirt 3","One of our newest style shirts","36€","Women","Shirt")
women_clothes4=Clothes("Sweatshirt 1","One of our newest style sweatshirts","25€","Women","Sweatshirt")
women_clothes5=Clothes("Sweatshirt 2","One of our newest style sweatshirts","47€","Women","Sweatshirt")
women_clothes6=Clothes("Sweatshirt 3","One of our newest style sweatshirts","56€","Women","Sweatshirt")

# Men bag objects
men_bags1=Bags("Belt Bag 1","One of our comfortable waist bag models","55£","Men","Belt Bag")
men_bags2=Bags("Belt Bag 2","One of our comfortable waist bag models","58£","Men","Belt Bag")
men_bags3=Bags("Belt Bag 3","One of our comfortable waist bag models","63£","Men","Belt Bag")
men_bags4=Bags("Handbag 1","One of our comfortable handbag models","21£","Men","Handbag")
men_bags5=Bags("Handbag 2","One of our comfortable handbag models","13£","Men","Handbag")
men_bags6=Bags("Handbag 3","One of our comfortable handbag models","18£","Men","Handbag")
men_bags7=Bags("Shoulder Bag 1","One of our comfortable shoulder bag models","12£","Men","Shoulder Bag")
men_bags8=Bags("Shoulder Bag 2","One of our comfortable shoulder bag models","15£","Men","Shoulder Bag")
men_bags9=Bags("Shoulder Bag 3","One of our comfortable shoulder bag models","18£","Men","Shoulder Bag")

# School bag objects
school_bags1=Bags("School Bag 1","One of our most stylish school bags models","15€","Non-Gender","School Bag")
school_bags2=Bags("School Bag 2","One of our most stylish school bags models","17€","Non-Gender","School Bag")
school_bags3=Bags("School Bag 3","One of our most stylish school bags models","19€","Non-Gender","School Bag")

# Women bag objects
women_bags1=Bags("Evening Bag 1","One of our comfortable waist bag models","75£","Women","Evening Bag")
women_bags2=Bags("Evening Bag 2","One of our comfortable waist bag models","118£","Women","Evening Bag")
women_bags3=Bags("Evening Bag 3","One of our comfortable waist bag models","93£","Women","Evening Bag")
women_bags4=Bags("Handbag 1","One of our comfortable handbag models","21£","Women","Handbag")
women_bags5=Bags("Handbag 2","One of our comfortable handbag models","13£","Women","Handbag")
women_bags6=Bags("Handbag 3","One of our comfortable handbag models","18£","Women","Handbag")
women_bags7=Bags("Shoulder Bag 1","One of our comfortable shoulder bag models","12£","Women","Shoulder Bag")
women_bags8=Bags("Shoulder Bag 2","One of our comfortable shoulder bag models","15£","Women","Shoulder Bag")
women_bags9=Bags("Shoulder Bag 3","One of our comfortable shoulder bag models","18£","Women","Shoulder Bag") 