from tkinter import * 
import tkinter as tk
import pymysql.cursors
import time
from tkinter import messagebox
from PIL import Image, ImageTk

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

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#---Mysql Connection Start
db = pymysql.connect(host='localhost',
                     user='root',
                     password='feyzullah0348', 
                     db='dbshoppingordersystem',
                     cursorclass=pymysql.cursors.DictCursor)
connection = db.cursor()
#---Mysql Connection End

global screen_names,continue_search
screen_names = []
continue_search = []

#---Messages 
def succesMessage():
    messagebox.showinfo("Succes","Operation Successful!")

def errorMessage():
    messagebox.showinfo("Error","Operation Failed!")

def notEmptyMessage():
    messagebox.showinfo("Error!","This field cannot be empty")

#---Tuple tipinden string'e dönüştürme için fonksyion
def convertTupleName(tup):
  pizza_name = ''.join(tup)
  return pizza_name

#---List yapısından string'e dönüştürme için fonskiyon
def convertList(lis):
  sosListe = ''.join(lis)
  return sosListe


#---Home Page Start
#---Login olmadan herkesin standrat göreceği ekranımız
def homePage():
    global home_screen
    home_screen = Tk()
    home_screen.title("Shopping Home Page")
    home_screen.geometry("1900x1000+1+1")
    home_screen.config(bg='white')
    home_screen.resizable(False,False)

    scrollbar = Scrollbar(home_screen, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)
    def scroll_window(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas = Canvas(home_screen, yscrollcommand=scrollbar.set)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=canvas.yview)
    canvas.bind_all("<MouseWheel>", scroll_window)



#--Logo
    imagea = Image.open("./images/Logo2.png")
    imagea = imagea.resize((100,66),Image.ANTIALIAS)
    imagea = ImageTk.PhotoImage(imagea)
    label1 = Label(home_screen, image=imagea)
    label1.place(x =20,y = 3)
    
#Top Bar
    label = Label(home_screen,background='white',width=250,height=4)
    label.place(x =120,y = 5)
    
    Button(home_screen, text="Home Page",activebackground="lightgray", borderwidth=0,font="verdana 11 bold",bg="white").place(x = 650, y = 25)
    Button(home_screen, text="About",activebackground="lightgray", borderwidth=0,font="verdana 11 bold",bg="white").place(x =850, y = 25)
    Button(home_screen, text="Contact",activebackground="lightgray", borderwidth=0,font="verdana 11 bold",bg="white").place(x = 1000, y = 25)
    Button(home_screen, text="Addresses",activebackground="lightgray", borderwidth=0,font="verdana 11 bold",bg="white").place(x = 1150, y = 25)

#----Categories
    Label(home_screen,text="__________________________",font="verdana 11 bold").place(x=20,y=100)
    Label(home_screen,text="Kategoriler",font="verdana 11 bold").place(x=20,y=90)

#Commandı Eklenmeyen Kategori buttonları.
    Label(home_screen,text="Men 🡶",font="verdana 11 bold").place(x=40,y=130)
    Button(home_screen, text="Giyim",activebackground="lightgray", borderwidth=0,font="verdana 11 bold").place(x = 70, y = 160)
    Button(home_screen, text="Ayakkabı",activebackground="lightgray", borderwidth=0,font="verdana 11 bold").place(x = 70, y = 190)
    Button(home_screen, text="Saat",activebackground="lightgray", borderwidth=0,font="verdana 11 bold").place(x = 70, y = 220)
    Button(home_screen, text="Çanta",activebackground="lightgray", borderwidth=0,font="verdana 11 bold").place(x = 70, y = 250)
    Label(home_screen,text="Women 🡶",font="verdana 11 bold").place(x=40,y=340)
    Button(home_screen, text="Giyim",activebackground="lightgray", borderwidth=0,font="verdana 11 bold").place(x = 70, y = 370)
    Button(home_screen, text="Ayakkabı",activebackground="lightgray", borderwidth=0,font="verdana 11 bold").place(x = 70, y = 400)
    Button(home_screen, text="Saat",activebackground="lightgray", borderwidth=0,font="verdana 11 bold").place(x = 70, y = 430)
    Button(home_screen, text="Çanta",activebackground="lightgray", borderwidth=0,font="verdana 11 bold").place(x = 70, y = 460)
    Button(home_screen, text="Login",activebackground="lightgray",bg='#008CBA',command=go_login, borderwidth=0,font="verdana 12 bold").place(x = 1680, y = 25)
    Button(home_screen, text="Register",activebackground="lightgray",bg='#008CBA',command=go_register ,borderwidth=0,font="verdana 12 bold").place(x = 1760, y = 25)

#----------------------------------------------------------------------------------------------------------------
    image1 = Image.open("./images/men_shoes_photo1.jpeg")
    image1 = ImageTk.PhotoImage(image1)
    image2 = Image.open("./images/men_shoes_photo1.jpeg")
    image2 = ImageTk.PhotoImage(image2)
    image3 = Image.open("./images/men_shoes_photo1.jpeg")
    image3 = ImageTk.PhotoImage(image3)
    image4 = Image.open("./images/men_shoes_photo1.jpeg")
    image4 = ImageTk.PhotoImage(image4)

    image5 = Image.open("./images/men_shoes_photo1.jpeg")
    image5 = ImageTk.PhotoImage(image5)
    image6 = Image.open("./images/men_shoes_photo1.jpeg")
    image6 = ImageTk.PhotoImage(image6)
    image7 = Image.open("./images/men_shoes_photo1.jpeg")
    image7 = ImageTk.PhotoImage(image7)
    image8 = Image.open("./images/men_shoes_photo1.jpeg")
    image8 = ImageTk.PhotoImage(image8)
    
    image9 = Image.open("./images/men_shoes_photo1.jpeg")
    image9 = ImageTk.PhotoImage(image9) 
    image10 = Image.open("./images/men_shoes_photo1.jpeg")
    image10 = ImageTk.PhotoImage(image10)
    image11 = Image.open("./images/men_shoes_photo1.jpeg")
    image11 = ImageTk.PhotoImage(image11)
    image12 = Image.open("./images/men_shoes_photo1.jpeg")
    image12 = ImageTk.PhotoImage(image12)

    #---Bilgi metinleri
    text1 = men_shoes1.description+'\n'+men_shoes1.type+'\n'+men_shoes1.price
    text2 = men_shoes2.description+'\n'+men_shoes2.type+'\n'+men_shoes2.price
    text3 = men_shoes3.description+'\n'+men_shoes3.type+'\n'+men_shoes3.price
    text4 = men_shoes4.description+'\n'+men_shoes4.type+'\n'+men_shoes4.price
    
    text5 = men_shoes5.description+'\n'+men_shoes5.type+'\n'+men_shoes5.price
    text6 = men_shoes6.description+'\n'+men_shoes6.type+'\n'+men_shoes6.price
    text7 = men_shoes7.description+'\n'+men_shoes7.type+'\n'+men_shoes7.price
    text8 = men_shoes8.description+'\n'+men_shoes8.type+'\n'+men_shoes8.price

    text9 = men_shoes9.description+'\n'+men_shoes9.type+'\n'+men_shoes9.price
    text10 = men_shoes10.description+'\n'+men_shoes10.type+'\n'+men_shoes10.price
    text11 = men_shoes11.description+'\n'+men_shoes11.type+'\n'+men_shoes11.price
    text12 = men_shoes12.description+'\n'+men_shoes12.type+'\n'+men_shoes12.price
    
#---resim ve açıklama için Label widget'ı oluşturun
    label1 = Label(home_screen, image=image1, text=text1, compound="top")
    label1.place(x = 400,y = 110)

    label2 = Label(home_screen, image=image2, text=text2, compound="top")
    label2.place(x = 690,y = 110)

    label3 = Label(home_screen, image=image3, text=text3, compound="top")
    label3.place(x = 980,y = 110)

    label4 = Label(home_screen, image=image4, text=text4, compound="top")
    label4.place(x = 1270,y = 110)
#--
    label5 = Label(home_screen, image=image5, text=text5, compound="top")
    label5.place(x = 400,y = 380)

    label6 = Label(home_screen, image=image6, text=text6, compound="top")
    label6.place(x = 690,y = 380)

    label7 = Label(home_screen, image=image7, text=text7, compound="top")
    label7.place(x = 980,y = 380)

    label8 = Label(home_screen, image=image8, text=text8, compound="top")
    label8.place(x = 1270,y = 380)
#--
    label9 = Label(home_screen, image=image9, text=text9, compound="top")
    label9.place(x = 400,y = 670)

    label10 = Label(home_screen, image=image10, text=text10, compound="top")
    label10.place(x = 690,y = 670)

    label11 = Label(home_screen, image=image11, text=text11, compound="top")
    label11.place(x = 980,y = 670)

    label12 = Label(home_screen, image=image12, text=text12, compound="top")
    label12.place(x = 1270,y = 670)

    home_screen.mainloop()
#---Home Page End

#---Login olduktan sonra ekranda gelecek ana ekranımız
def loginverifyandhomepage():
    global home_screen_real
    home_screen_real = Tk()
    home_screen_real.title("Shopping Home Page")
    home_screen_real.geometry("1900x1000+1+1")
    home_screen_real.config(bg='white')
    home_screen_real.resizable(False,False)

    scrollbar = Scrollbar(home_screen_real, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)
    def scroll_window(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas = Canvas(home_screen_real, yscrollcommand=scrollbar.set)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=canvas.yview)
    canvas.bind_all("<MouseWheel>", scroll_window)

# #--Logo
#     image1 = Image.open("./images/Logo.png")
#     image1 = ImageTk.PhotoImage(image1)

#     label1 = Label(home_screen_real, image=image1,compound="top",width=250,height=250)
#     label1.place(x =20,y = 20)

#---- Categories
    Label(home_screen_real,text="__________________________",font="verdana 11 bold").place(x=20,y=70)
    Label(home_screen_real,text="Kategoriler",font="verdana 11 bold").place(x=20,y=60)

#Commandı Eklenmeyen Kategori buttonları
    Label(home_screen_real,text="Erkek 🡶",font="verdana 11 bold").place(x=40,y=100)
    Button(home_screen_real, text="Giyim",activebackground="lightgray", borderwidth=0,font="verdana 11 bold").place(x = 70, y = 130)
    Button(home_screen_real, text="Ayakkabı",activebackground="lightgray", borderwidth=0,font="verdana 11 bold").place(x = 70, y = 160)
    Button(home_screen_real, text="Saat",activebackground="lightgray", borderwidth=0,font="verdana 11 bold").place(x = 70, y = 190)
    Button(home_screen_real, text="Çanta",activebackground="lightgray", borderwidth=0,font="verdana 11 bold").place(x = 70, y = 220)
    Label(home_screen_real,text="Kadın 🡶",font="verdana 11 bold").place(x=40,y=310)
    Button(home_screen_real, text="Giyim",activebackground="lightgray", borderwidth=0,font="verdana 11 bold").place(x = 70, y = 340)
    Button(home_screen_real, text="Ayakkabı",activebackground="lightgray", borderwidth=0,font="verdana 11 bold").place(x = 70, y = 370)
    Button(home_screen_real, text="Saat",activebackground="lightgray", borderwidth=0,font="verdana 11 bold").place(x = 70, y = 400)
    Button(home_screen_real, text="Çanta",activebackground="lightgray", borderwidth=0,font="verdana 11 bold").place(x = 70, y = 430)
    Button(home_screen_real, text="🛒",activebackground="lightgray", borderwidth=0,font="verdana 20 bold").place(x =1800, y = 40)

#----------------------------------------------------------------------------------------------------------------
    image1 = Image.open("./images/men_shoes_photo1.jpeg")
    image1 = ImageTk.PhotoImage(image1)
    image2 = Image.open("./images/men_shoes_photo1.jpeg")
    image2 = ImageTk.PhotoImage(image2)
    image3 = Image.open("./images/men_shoes_photo1.jpeg")
    image3 = ImageTk.PhotoImage(image3)
    image4 = Image.open("./images/men_shoes_photo1.jpeg")
    image4 = ImageTk.PhotoImage(image4)
    
    image5 = Image.open("./images/men_shoes_photo1.jpeg")
    image5 = ImageTk.PhotoImage(image5)
    image6 = Image.open("./images/men_shoes_photo1.jpeg")
    image6 = ImageTk.PhotoImage(image6)
    image7 = Image.open("./images/men_shoes_photo1.jpeg")
    image7 = ImageTk.PhotoImage(image7)
    image8 = Image.open("./images/men_shoes_photo1.jpeg")
    image8 = ImageTk.PhotoImage(image8)

    image9  = Image.open("./images/men_shoes_photo1.jpeg")
    image9  = ImageTk.PhotoImage(image9) 
    image10 = Image.open("./images/men_shoes_photo1.jpeg")
    image10 = ImageTk.PhotoImage(image10)
    image11 = Image.open("./images/men_shoes_photo1.jpeg")
    image11 = ImageTk.PhotoImage(image11)
    image12 = Image.open("./images/men_shoes_photo1.jpeg")
    image12 = ImageTk.PhotoImage(image12)

#---Bilgi metinleri
    text1 = men_shoes1.description+'\n'+men_shoes1.type+'\n'+men_shoes1.price
    text2 = men_shoes2.description+'\n'+men_shoes2.type+'\n'+men_shoes2.price
    text3 = men_shoes3.description+'\n'+men_shoes3.type+'\n'+men_shoes3.price
    text4 = men_shoes4.description+'\n'+men_shoes4.type+'\n'+men_shoes4.price
    
    text5 = men_shoes5.description+'\n'+men_shoes5.type+'\n'+men_shoes5.price
    text6 = men_shoes6.description+'\n'+men_shoes6.type+'\n'+men_shoes6.price
    text7 = men_shoes7.description+'\n'+men_shoes7.type+'\n'+men_shoes7.price
    text8 = men_shoes8.description+'\n'+men_shoes8.type+'\n'+men_shoes8.price

    text9  = men_shoes9.description+'\n'+men_shoes9.type+'\n'+men_shoes9.price
    text10 = men_shoes10.description+'\n'+men_shoes10.type+'\n'+men_shoes10.price
    text11 = men_shoes11.description+'\n'+men_shoes11.type+'\n'+men_shoes11.price
    text12 = men_shoes12.description+'\n'+men_shoes12.type+'\n'+men_shoes12.price

    #---Resim ve açıklama için Label widget'ı oluşturun
    label1 = Label(home_screen_real, image=image1, text=text1, compound="top")
    label1.place(x = 400,y = 90)

    label2 = Label(home_screen_real, image=image2, text=text2, compound="top")
    label2.place(x = 690,y = 90)

    label3 = Label(home_screen_real, image=image3, text=text3, compound="top")
    label3.place(x = 980,y = 90)

    label4 = Label(home_screen_real, image=image4, text=text4, compound="top")
    label4.place(x = 1270,y = 90)
#--
    label5 = Label(home_screen_real, image=image5, text=text5, compound="top")
    label5.place(x = 400,y = 420)

    label6 = Label(home_screen_real, image=image6, text=text6, compound="top")
    label6.place(x = 690,y = 420)

    label7 = Label(home_screen_real, image=image7, text=text7, compound="top")
    label7.place(x = 980,y = 420)

    label8 = Label(home_screen_real, image=image8, text=text8, compound="top")
    label8.place(x = 1270,y = 420)
#--
    label9 = Label(home_screen_real, image=image9, text=text9, compound="top")
    label9.place(x = 400,y = 750)
    
    label10 = Label(home_screen_real, image=image10, text=text10, compound="top")
    label10.place(x = 690,y = 750)

    label11 = Label(home_screen_real, image=image11, text=text11, compound="top")
    label11.place(x = 980,y = 750)

    label12 = Label(home_screen_real, image=image12, text=text12, compound="top")
    label12.place(x = 1270,y = 750)

    home_screen_real.mainloop()

#---Register Panel & Register Verify Control Start
def register_verify():
    name_surname_info = name_surname.get()
    age_info = age.get()
    phone_number_info = phone_number.get()
    email_info = email.get()
    address_info = address.get()
    password_info=password.get()

    if name_surname_info == " ":
        notEmptyMessage()
    elif age_info == " ":
        notEmptyMessage()
    elif phone_number_info == " ":
        notEmptyMessage()
    elif email_info == " ":
        notEmptyMessage()
    elif address_info == " ":
        notEmptyMessage()
    elif password_info == " ":
        notEmptyMessage()
    else:
        connection.execute("INSERT INTO registeruser VALUES (%s,%s,%s,%s,%s,%s,%s)",(None,name_surname_info,age_info,phone_number_info,email_info,address_info,password_info))
        db.commit()
        time.sleep(1)
        succesMessage()

#---Register Panel Screen
def registerPanel():
    global register_screen
    register_screen =Tk()
    register = "register"
    continue_search.append(register)
    register_screen.geometry("600x400+650+200")
    register_screen.title("Shopping Order System Register Panel")
    register_screen.config(bg='white')
    register_screen.resizable(False, False)
    
    global name_surname,age,phone_number,email,address,password

    Label(register_screen,text="_________________________________________",bg="white",font="verdana 11 bold").place(x=60,y=35)
    Label(register_screen,text="Register Form ",bg="white",font="verdana 11 bold").place(x=230,y=15)

    photo = PhotoImage(file="userRegister.png")
    Label(register_screen,image=photo,bd=2,highlightcolor="black",width=100,height=100).place(x=60,y=80)

    Label(register_screen,text="You have\naccount?",bg="white",font="verdana 8 bold").place(x=70,y=190)

    Button(register_screen, text="Login Here!", bg="#008CBA",command=loginButton, fg="white", font=("Helvetica", 9), width=10, height=0, bd=0,borderwidth=1,highlightthickness=2).place(x=70,y=230)
    Button(register_screen, text="Continue Search", bg="#008CBA",fg="white", command=continue_search_page ,font=("Helvetica", 8), width=12, height=0, bd=0,borderwidth=1,highlightthickness=2).place(x = 70, y = 260)

    Label(register_screen,text="Name Surname: ",bg="white",font="verdana 8 bold").place(x=180,y=80)
    name_surname = StringVar()
    Entry(register_screen,textvariable=name_surname,bg="white",font="verdana 8 bold",borderwidth=1,highlightthickness=2).place(x=300,y=80)

    Label(register_screen,text="Age: ",bg="white",font="verdana 8 bold").place(x = 180, y = 110)
    age = StringVar()
    Entry(register_screen,textvariable=age,bg="white",font="verdana 8 bold",borderwidth=1,highlightthickness=2).place(x=300,y = 110)

    Label(register_screen,text="Phone Number: ",bg="white",font="verdana 8 bold").place(x=180,y=140)
    phone_number = StringVar()
    Entry(register_screen,textvariable=phone_number,font="verdana 8 bold",borderwidth=1,highlightthickness=2).place(x=300,y=140)

    Label(register_screen,text="E-Mail: ",bg="white",font="verdana 8 bold").place(x=180,y=170)
    email=StringVar()
    Entry(register_screen,textvariable=email,font="verdana 8 bold",borderwidth=1,highlightthickness=2).place(x=300,y=170)

    Label(register_screen,text="Address: ",bg="white",font="verdana 8 bold").place(x=180,y=200)
    address = StringVar()
    Entry(register_screen,textvariable=address,font="verdana 8 bold",borderwidth=1,highlightthickness=2).place(x=300,y=200)

    Label(register_screen,text="Password: ",bg="white",font="verdana 8 bold").place(x=180,y=230)
    password=StringVar()
    Entry(register_screen,textvariable=password,font="verdana 8 bold",borderwidth=1,highlightthickness=2).place(x=300,y=230)

    Button(register_screen, text="Register", bg="#008CBA",command=register_verify, fg="white", font=("Helvetica", 10), width=10, height=0, bd=0,borderwidth=1,highlightthickness=2).place(x =330,y=260)

    register_screen.mainloop()
#---Register Panel & Register Verify Control End


#---Routing Buttons Start
def loginButton():
    register_screen.destroy()
    loginPanel()

def registerButton():
    login_screen.destroy()
    registerPanel()

def continue_search_page():
    print(continue_search)
    if 'register' in continue_search:
        register_screen.destroy()
        continue_search.clear()
        homePage()

    if 'login' in continue_search:
        login_screen.destroy()
        continue_search.clear()
        homePage()

def go_login():
    home_screen.destroy()
    loginPanel()

def go_register():
    home_screen.destroy()
    registerPanel()
#---Routing Buttons End


#---Login Panel & Login Verify Control Start
def login_verify():
    email_info = email.get()
    password_info = password.get()

    if email_info == " ":
        notEmptyMessage()
    elif password_info == " ":
        notEmptyMessage()
    else:
        sql = "SELECT * FROM registeruser where email = %s and password = %s"
        connection.execute(sql,[(email_info),(password_info)])
        db.commit()
        result = connection.fetchall()
        if result:
            for i in result:
                succesMessage()
                login_screen.destroy()
                loginverifyandhomepage()
        else:
            errorMessage()

def loginPanel():
    global login_screen
    login_screen =Tk()
    login = "login"
    continue_search.append(login)
    login_screen.geometry("600x400+650+200")
    login_screen.title("Shopping Order System Login Panel")
    login_screen.config(bg='white')
    login_screen.resizable(False, False)
    
    Label(login_screen,text="_________________________________________",bg="white",font="verdana 11 bold").place(x=60,y=35)
    Label(login_screen,text="Login Form ",bg="white",font="verdana 11 bold").place(x=230,y=15)

    photo = PhotoImage(file="userLogin.png")
    Label(login_screen,image=photo,bd=2,highlightcolor="black",width=100,height=100).place(x=60,y=80)
    Label(login_screen,text="You not have\naccount?",bg="white",font="verdana 8 bold").place(x=70,y=190)
    Button(login_screen, text="Register Here!", bg="#008CBA",command=registerButton, fg="white", font=("Helvetica", 9), width=11, height=0, bd=0,borderwidth=1,highlightthickness=2).place(x=70,y=230)
    Button(login_screen, text="Continue Search", bg="#008CBA",fg="white", command=continue_search_page ,font=("Helvetica", 8), width=12, height=0, bd=0,borderwidth=1,highlightthickness=2).place(x = 70, y = 260)

    global email,password

    Label(login_screen,text="E-Mail: ",bg="white",font="verdana 8 bold").place(x=180,y=100)
    email = StringVar()
    Entry(login_screen,textvariable=email,bg="white",font="verdana 8 bold",borderwidth=1,highlightthickness=2).place(x=300,y=100)

    Label(login_screen,text="Password: ",bg="white",font="verdana 8 bold").place(x = 180, y = 130)
    password = StringVar()
    Entry(login_screen,textvariable=password,bg="white",font="verdana 8 bold",borderwidth=1,highlightthickness=2).place(x=300,y = 130)
    
    Button(login_screen, text="Login", bg="#008CBA",command=login_verify, fg="white", font=("Helvetica", 10), width=10, height=0, bd=0,borderwidth=1,highlightthickness=2).place(x =330,y=160)

    login_screen.mainloop()
#--- Login Panel & Login Verify Control End 
#--- registerPanel()

homePage()
