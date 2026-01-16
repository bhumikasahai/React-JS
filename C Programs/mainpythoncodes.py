#1. Python Data Expressions and Operators

#To print the sum of two numbers
'''a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
print("The sum is= ",a+b)'''

#To find the area of the cirle
'''r=float(input("Enter the radius "))
area=3.14*(r**2)
print("The area is= ",area)'''

#To print the average of first two highest marks among three
'''a=int(input("Enter the marks1"))
b=int(input("Enter the marks2"))
c=int(input("Enter the marks3"))
avg1=(a+b)/2
avg2=(b+c)/2
avg3=(a+c)/2
if(avg1>avg3 and avg1>avg2):
    print(avg1,"avg1")
elif(avg2>avg3 and avg2>avg1):
    print(avg2,"avg2")
elif(avg3>avg1 and avg3>avg2):
    print(avg3,"avg3")
else:
    print("Invalid input")'''

#Multiply a given number by bitwise operator
'''n=int(input("Enter the number"))
y=n<<2
print(y)'''

#To perform Bitwise negation 
'''n=int(input("Enter the number "))
y=~n
print(y)'''

# Conditional Statements

#To check whether the entered alphabet is vowel or constant
'''vowel='aeiouAEIOU'
n=input("Enter the alphabet")
if n in vowel:
    print("It is a vowel",n)
else:
    print("It is a consonant")'''

#To print the largest among 3 numbers
'''a=int(input("Enter the first number"))
b=int(input("Enter the second number "))
c=int(input("Enter the third number "))
if a>b and a>c :
    print("a is largest ")
elif b>c and b>a:
    print("b is largest ")
elif(c>a and c>b):
    print("c is largest ")
else:
    print("equal")'''

#Check year is leap year or not
'''year=int(input("Enter the year"))
if year%4==0 or year%100==0 or year%400==0 :
    print("Leap year ",year)
else:
    print("Not a leap year")'''

#Accept two characters and check whether they are equal or not
'''a=input("Enter the first character ")
b=input("Enter the second caracter ")
if a==b:
    print("Equal characters")
else:
    print("Not equal characters ")'''

#Print the factorial number
'''a=int(input("Enter the number "))
fact=1
if a<0:
    print("Factorial doesnt exist")
elif a==0 :
    print("Factorial is 1 ")
elif a>0:
    for i in range(1,a+1):
        fact=fact*i  
    print(fact)'''

# Control Statements

#To print the countdown using while loop
'''n=int(input("Enter the number "))
while n>=0:
    print(n)
    n=n-1'''

#To print the reverse of a number
'''n=int(input("Enter the number "))
b=str(n)
y=int(b[ : :-1])
print("Reversed number is ",y)'''

#To print the fibonacci series
'''n=int(input("Enter the n number of terms "))
n1=0
n2=1
print(n1)
while n1<=n :
    n1,n2=n2,n1+n2
    print(n1)'''

#Create a list and all the items in it
'''a=[]
n=int(input("Enter the list size "))
for i in range(0,n):
    print("Enter the item at index",i)
    it=input()
    a.append(it)
print("The list is: ",a)'''

#Print the reverse of the list
'''a=['i','me','myself','mine']
print("The original list is: ",a)
print("The reversed list is:",a[::-1])'''

#To print the odd position elements from the list
'''a=[]
n=int(input("Enter the list size "))
for i in range(0,n):
    print("Enter the item at index",i)
    it=input()
    a.append(it)
print("The list is: ",a)
for i in range(a,len(a)):
    if i%2!=0:
        print(a[i])'''

# Strings In Python , Indexing and Slicing

#Program to demonstrate indexing and slicing
'''a=input("Enter the string ")
print(a[3])
print(a[2:4])'''

#Replace the vowel by _
'''a=input("Enter the string ")
vowel="aeiouAEIOU"
for i in range(len(a)):
    if a[i] in vowel:
        print(a[i],end="")
    else:
        print("_",end="")'''

#To split the sentence
'''a=input("Enter the string ")
b=a.split()
for i in range(len(b)):
    b[i]=b[i].upper()
print(b)'''

#To check whether the given string is palindrome or not
'''a=input("Enter the string ")
b=a[::-1]
if a==b:
    print("Palindrome")
else:
    print("Not Palindrome")'''

# Tuples and Sets with Library Functions

#Create a tuple and perform various methods
'''t=(1,2,3,4,5)
for i in t:
    print(i)
x=input("Enter something")
if x in t:
    print(x,"in tupple")
else:
    print(x,"not i tupple")
t.add("9")
print(t)'''

#Write a python program to find replaced items in a tuple
'''t=(1,2,3,3,4,5)
l=[]
for i in t:
    if t.count(i)>1:
        if i not in l:
            l.append(i)
print("Repeated items are: ")
print(l)'''

#Python program to create a set and perform various methods
'''set1={"apple","banana","cherry"}
for x in set1:
    print(x)
i=input("Enter something ")
if i in set1 :
    print(i,"in tupple ")
else:
    print("not in a tuppple ")
set1.add("orange")
print(set1)'''

#Program which tells which letters are present in both the strings
'''string1="hello"
string2="namaste"
e=list(set(string1)^set(string2))
print("The letters are: ")
for i in e:
    print(i)'''

# Dictionary in Python with Library Funcions

#Generate a dictionary and prints number from 1 to n
'''n=int(input("Enter the n number fo terms: "))
d={}
for i in range(1,n+1):
    d[i]= i*i
print(d)'''

#Create a dictionary and perform various methods
'''d={"brand":"Suzuki","model":"Dzire","year":"1992"}
print(d)
x=d["model"]
print(x)
y=d.get("model")
print(y)
d["year"]=2018
print(d)
z=len(d)
print(z)'''

# COURSE PACK

#Read two numbers and print their quotient and remainder
'''a=int(input("Enter the first number "))
b=int(input("Enter the second number "))
quotient=a/b
remainder=a%b
print("The remainder is : ",remainder)
print("The uotient is : ",quotient)'''

#Print odd numbers from 1-20
'''n=int(input("Enter the n no of terms: "))
for i in range(0,n):
    if i%2!=0:
        print(i,end=" ")'''

#Armstrong number
'''n=int(input("Enter the number: "))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum=sum+(digit**3)
    temp=temp//10
if(n==sum):
    print("Armstrong no")
else:
    print("No armstrong")'''

#Sequence
'''n=int(input("Enter the n no of terms: "))
for i in range(0,n,+5):
    print(i,end=" ")'''

#String and uppercase letters 
'''string="My name is Bhumika Sahai"
up=0
lo=0
for i in string:
    if i==" " :
        continue
    if i.islower():
        lo=lo+1
    if i.isupper():
        up=up+1
print("lowercase:",lo)
print("uppercase: ",up)'''

#Print the even numbers from the list
'''l1=[1,3,3,4,5,6,7,8,9]
l2=[]
for i in range(len(l1)):
    if l1[i]%2==0 :
        print(l1[i])
        l2.append(l1[i])
print(l2)'''

#Count the words,digits and characters
'''st="I love python 24 @1"
v=d=s=c=0
for i in range(len(st)):
    if (st[i].isdigit()):
        d=d+1
    elif (st[i]==" "):
        s=s+1
    elif (st[i] in 'aeiouAEIOU'):
        v=v+1
    else:
        c=c+1
print(d)
print(s)
print(c)
print(v)'''

#Join and split in strings
'''st1="happy"
st2="weekend"
x=st1+st2
print(x)
txt = "welcome to the jungle"
y = txt.split()
print(y)'''

#Print negative no in a list
'''l1=[1,2,3,-1,-2,-3]
for i in range(len(l1)):
    if l1[i]<0 :
        print(l1[i])'''

#Create a tuple from a list
'''l=[1,2,3,4]
tup=tuple(l)
l2=[]
print(tup)
for i in range(len(l)):
    l2.append((l[i])**3)
newtup=tuple(l2)
print(newtup)'''

#Extract digits from tuple
'''t=(1,2,3,45)
for i in range(len(t)):
    if t(i).isdigit() :
        print(t[i])'''

#Program to check common and uncommon letters in a string
'''st1="sahai"
st2="bhumika"'''




#Merging of two dictionaries
'''dict1={"name":"bhumika","age":"18","caste":"general"}
dict2={"height":"5.5","hobbies":"sleeping"}
x={}
x=dict1.update(dict2)
print(x)'''

#Multiply the elements in a dictionary


#Check whether a given key exists in a dictionary


#Count of words appearing in string using dictionary


#Repeated item in a tuple
'''t=(1,2,3,4,3,5,5)
l=[]
for i in t:
    if t.count(i)>1:
        if i not in l:
            l.append(i)
print("Repated items are: ")
print(l)'''

#Create a set and peform various methods
'''set1={"apple","banana","cherry"}
for x in set1:
    print(x)
i=input("Enter something")
if i in set1:
    print(i,"in set1")
else:
    print(i,"not in set1")
set1.add("guava")
print(set1)'''

#Create a dictionary and perform various methods
'''dict={"name":"bhumika","age":18,"caste":"general"}
print(dict)
x=dict["age"]
y=dict.get("name")
print(y)
print(x)
dict["age"]=19
print(dict)
z=len(dict)
print(z)'''





# SEMESTER 2
#OBJECT AND CLASSES (OOPS IN PYTHON)

# Without Constructor 
'''class person:
    name="Bhumika"
    occ="Student"
    networth=0
    def info(self):
        print(f"{self.name} is a {self.occ}")

a=person()
b=person()
a.name="Bakshi"
a.occ="Annoy"

b.name="Vidushi"
b.occ="Sleeping"
a.info()
b.info()'''

# With Constructor (parameters one)
'''class person:
    def __init__(self,n,o):
        print("Hey im a person")
        self.name = n
        self.occ = o
    def info(self):
        print(f"{self.name} is a {self.occ}")

a=person("Bhumika","student")
b=person("Bakshi","annoy")
a.info()
b.info()'''

#default program (self) 
'''class person:
    def __init__(self):
        print("Hey im a person")
    def info(self):
        print(f"{self.name} is a {self.occ}")
a=person()
b=person()'''


'''class CarDesign:
    pass
obj_1=CarDesign()
obj_2=CarDesign()
print(type(obj_1))
print(type(obj_2))'''


'''class Instructor:
    pass
obj_1 = Instructor()
obj_1.name="Bhumika"
obj_1.address="Kanpur"
print(obj_1.name)
obj_2 = Instructor()
obj_2.name="Ojasvi"
obj_2.address="Delhi"
print(obj_2.name)'''


'''class Instructor:
    def __init__(self):
        print("Creating a new object")
obj_1 = Instructor()
obj_1.name="Bhumika"
obj_1.address="Kanpur"
print(obj_1.name)
obj_2 = Instructor()
obj_2.name="Ojasvi"
obj_2.address="Delhi"
print(obj_2.name)'''


'''class Instructor:
    followers =0
    def __init__(self,ins_name,address):
        self.name=ins_name
        self.address=address
    def display(self,sub_name):
        print(f"Hi, I am {self.name} and I teach {sub_name}")
    def update_followers(self,follower_name):
        self.followers +=1

obj1=Instructor("Bhumika","Kanpur")
print(obj1.name)
obj1.display("Python")
obj1.update_followers("Payal")
print(obj1.followers)

obj2=Instructor("Ojasvi","Delhi")
obj2.update_followers("Yash")
print(obj2.followers)'''

''''class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
        self.area= self.pi*radius*radius
    def get_circumference(self):
        return 2 * self.pi * self.radius

circle_1= Circle(4)
print(circle_1.get_circumference())
circle_2= Circle(14)
print(f"The circumference of circle is : {circle_2.get_circumference()}")
print(f"The area of circlem is : {circle_1.area}")'''

'''class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def get_Area(self):
        return self.length * self.breadth
rect_1=Rectangle(6,4)
print(f"The area of rectangle is : {rect_1.get_Area()}")'''

'''class Students:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
student1=Students("Bhumika",18,"A+")
print(student1.name)
print(student1.age)
print(student1.grade)'''

'''class Students:
    pass
obj1=Students()'''

'''class Staff:
    def __init__(self,post):
        self.post=post
class Teacher(Staff):
    def __init__(self, post, name, subject):
        super().__init__(post)  # Call the initializer of the superclass
        self.name = name
        self.subject = subject
    def display_info(self):
        print(f"My {self.post} name is {self.name} and she teaches {self.subject}")
teacher1=Teacher("teacher","promita","maths")
teacher1.display_info()'''

'''class Vehicle:
    def __init__(self,speed,mileage):
        self.max_speed=speed
        self.mileage=mileage
    def display_info(self):
        print(f"The vehicle's speed is {self.max_speed}km/hr and its mileage is {self.mileage}")
vehicle1=Vehicle(180,80)
vehicle1.display_info()'''

'''class Person:
    year=2024
    age=0
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.date_of_birth=dob
    def get_age(self):
        age=self.year-self.date_of_birth
        print(f"Person's age as of {self.year} year is {age}")
person1=Person("Bhumika","India",2005)
person1.get_age()
print(person1.name)
print(person1.country)'''

'''class BankAccount:
    def __init__(self,accountNo,name,balance):
        self.acc_no=accountNo
        self.name=name
        self.balance=balance
    def display_info(self):
        print(f"Account Number is {self.acc_no} and the name of the owner is {self.name} with the balance {self.balance}")
bk_1=BankAccount(1010766,"Bhumika",15000)
bk_1.display_info()'''

'''class Vehicle:
    def __init__(self,fare,maintaineance):
        self.fare=fare
        self.maint_charge=maintaineance
class Bus(Vehicle):
    def __init__(self,fare,maintaineance):
        super().__init__(fare,maintaineance)
    def display_info(self):
        print(f"The bus' fare is {self.fare} and its maintaineance is {self.maint_charge}")
bus1=Bus(10000,1100)
bus1.display_info()'''

'''class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Mammal(Animal):
    def __init__(self,name,age,fur_colour):
        super().__init__(name,age)
        self.fur_colour=fur_colour
    def make_sound(self):
        return ("Mammals make various sounds")
class Bird(Animal):
    def __init__(self,name,age,wing_span):
        super().__init__(name,age)
        self.wing_span=wing_span
    def fly(self):
        return (f"{self.name} is flying")
dog=Mammal("tommy",5,"brown")
print (dog.name)
print(dog.age)
print(dog.fur_colour)
print(dog.make_sound)

sparrow=Bird("Eagle",3,6)
print(sparrow.name)
print(sparrow.age)
print(sparrow.wing_span)
sparrow.fly'''

'''class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
class Car(Vehicle):
    def __init__(self,make,model,year,seating_capacity):
        super().__init__(make,model,year)
        self.seating_capacity=seating_capacity
class Truck(Vehicle):
    def __init__(self,make,model,year,cargo_capacity):
        super().__init__(make,model,year)
        self.cargo_capacity=cargo_capacity
class Motorcycle(Vehicle):
    def __init__(self,make,model,year,sound):
        super().__init__(make,model,year)
        self.sound=sound

car=Car("Suzuki","Alto",2001,4)
print(car.make)
print(car.model)
print(car.year)
print(car.seating_capacity)

truck=Truck("Tata","tatagold",2015,"5 ton")
print(truck.make)
print(truck.model)
print(truck.year)
print(truck.cargo_capacity)


bike=Motorcycle("TVS","spelender",2000,"woaa woaa")
print(bike.make)
print(bike.model)
print(bike.year)
print(bike.sound)'''


'''class FileProcessor:
    def _init_(self, file_name):
        self.file_name = file_name

    def read_file(self):
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    print(line.strip())  # Process each line of the file
        except FileNotFoundError as e:
            print(f"File not found: {e}")
            # Provide suggestions or prompt user for correct filename
        except PermissionError as e:
            print(f"Permission denied: {e}")
            # Provide suggestions or prompt user to check file permissions
        except IOError as e:
            print(f"I/O error: {e}")
            # Log the error details and provide suggestions for troubleshooting


# Example usage:
file_name="sales_datacsv"
  # Example filename provided by the user
processor = FileProcessor(file_name)
processor.read_file()'''


'''class Shape:
    pi=3.14
    area=1
    def __init__(self,radius):
        self.radius=radius
class Rectangle(Shape):
    def __init__(self,radius,lenght):
        super().__init__(radius)
        self.length=lenght
    def display(self):
        area=self.length * self.radius
        print(f" the area is: {area}")
class Circle(Shape):
    def __init__(self,radius):
        super().__init__(radius)
        pass
    def display(self):
        area=self.pi*self.radius*self.radius
        print(f" The area is {area}")
class Triangle(Shape):
    def __init__(self,radius,height):
        super().__init__(radius)
        self.height=height
    def display(self):
        area = 0.5*self.radius*self.height
        print(f"The area is {area}")

rect=Rectangle(5,4)
rect.display()

circle=Circle(5)
circle.display()

triangle=Triangle(10,5)
triangle.display()'''

'''from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class Lion(Animal):
    def make_sound(self):
        return "Roar"    
    def move(self):
        return "Walk"

class Monkey(Animal):
    def make_sound(self):
       return "Chatter"
    
    def move(self):
        return "Climb"

# Instantiating objects and demonstrating functionalities
lion = Lion()
monkey = Monkey()

print("Lion makes sound:", lion.make_sound())
print("Lion moves by:", lion.move())

print("Monkey makes sound:", monkey.make_sound())
print("Monkey moves by:", monkey.move())'''


#GRAPHIC USER INTERFACE

# 4 buttons

'''from tkinter import *
root = Tk()
root.geometry("644x344")
def hello():
    print("Hello!")
def name():
    print("Bhumika")
def full_name():
    print("Sahai")
def section():
    print("Section 1")
f1=Frame(root,borderwidth=6,bg="white",relief=SUNKEN)
f1.pack()
b1=Button(f1,fg="red",bg="white",text="Click 1",command=hello)
b1.pack(side=RIGHT)
b2=Button(f1,fg="red",bg="white",text="Click 2",command=name)
b2.pack(side=RIGHT)
b3=Button(f1,fg="red",bg="white",text="Click 3",command=full_name)
b3.pack(side=RIGHT)
b4=Button(f1,fg="red",bg="white",text="Click 4",command=section)
b4.pack(side=RIGHT)
root.mainloop()'''


# Widget and Grid

'''from tkinter import *
def getvals():
    print(uservalue.get())
    print(passvalue.get())
root=Tk()
root.geometry("655x344")
user=Label(root,text="username")
password=Label(root,text="password")
user.grid()
password.grid(row=1)
uservalue=StringVar()
passvalue=StringVar()
userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
Button(text="Submit",command=getvals).grid()
root.mainloop()'''

# DANCE FORM

'''from tkinter import *
root=Tk()
def getvals():
    print(namevalue.get())
    print(agevalue.get())
    print(danceformvalue.get())
    print(addressvalue.get())
root.geometry("700x400")
name=Label(root,text="fullname")
age=Label(root,text="Age")
danceform=Label(root,text="dance form")
address=Label(root,text="address")
name.grid()
age.grid(row=1)
danceform.grid(row=2)
address.grid(row=3)
agevalue=StringVar()
namevalue=StringVar()
danceformvalue=StringVar()
addressvalue=StringVar()
nameentry=Entry(root,textvariable=namevalue)
ageentry=Entry(root,textvariable=agevalue)
danceformentry=Entry(root,textvariable=danceformvalue)
addressentry=Entry(root,textvariable=addressvalue)
nameentry.grid(row=0,column=1)
ageentry.grid(row=1,column=1)
danceformentry.grid(row=2,column=1)
addressentry.grid(row=3,column=1)
Button(text="Submit",command=getvals).grid()
root.mainloop()'''

# PRIVACY 

'''from tkinter import *
root = Tk()
def getvals():
    print("IT WORKS")
root.geometry("700x400")
Label(root,text="Privacy is the Priority",font="comicsansm 13 bold").grid(row=0,column=5)
username=Label(root,text="Username")
password=Label(root,text="Password")

username.grid(row=1,column=2)
password.grid(row=2,column=2)

uservalue=StringVar()
passvalue=StringVar()
privacyvalue=IntVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)

userentry.grid(row=1,column=3)
passentry.grid(row=2,column=3)

#Checkbox 
privacy=Checkbutton(text="Want to have your privacy",variable=privacyvalue)
privacy.grid(row=3,column=2)

Button(text="Submit",command=getvals).grid (row=4,column=3)

root.mainloop()'''

# Events in Python

'''from tkinter import *
def bhumika(event):
    print(f"We clicked on the button at {event.x},{event.y}")
root=Tk()
root.title("Events in Tkinter")
root.geometry("644x344")
widget=Button(root,text="Click me please")
widget.pack()
widget.bind('<Button-1>',bhumika)
widget.bind('<Double-1>',quit)
root.mainloop()'''

# Menus and Submenus(1-command)
'''from tkinter import *
root=Tk()
root.geometry("766x544")
root.title("Pycharm")

def myfunc():
    print("I am a fumction")

mymenu=Menu(root)
mymenu.add_command(label="File",command=myfunc)
mymenu.add_command(label="Exit",command=quit)
root.config(menu=mymenu)

root.mainloop()'''

# Menus and Submenus(2-dropdown)
'''from tkinter import *
root=Tk()
root.geometry("766x544")
root.title("Pycharm")
def myfunc():
    print("I am a function")

mainmenu=Menu(root)

m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="Cut",command=myfunc)
m1.add_command(label="Copy",command=myfunc)
m1.add_separator()
m1.add_command(label="Paste",command=myfunc)
m1.add_command(label="Send",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m1)



m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="New Project",command=myfunc)
m2.add_command(label="Edit",command=myfunc)
m2.add_separator()
m2.add_command(label="Save",command=myfunc)
m2.add_command(label="Save As",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m2)

root.mainloop()'''

# Message Box
'''from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("766x544")
root.title("Pycharm")
def myfunc():
    print("I am a function")
def help():
    print("How may i help you?")
    tmsg.showinfo("Help","Bhumi will help you with the gui")
def rate():
    print("Rate us")
    value=tmsg.askquestion("You used this GUI ... was your experience good?")
    if value=="yes":
        msg="Rate us on the appstore"
    else:
        msg="Our helping member will call you soon"
    tmsg.showinfo("Experience",msg)

mainmenu=Menu(root)

m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="Cut",command=myfunc)
m1.add_command(label="Copy",command=myfunc)
m1.add_separator()
m1.add_command(label="Paste",command=myfunc)
m1.add_command(label="Send",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m1)



m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="New Project",command=myfunc)
m2.add_command(label="Edit",command=myfunc)
m2.add_separator()
m2.add_command(label="Save",command=myfunc)
m2.add_command(label="Save As",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m2)

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate",command=rate)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help",menu=m3)


root.mainloop()'''


# Slider 

'''from tkinter import *
import tkinter.messagebox as tmsg
def getdollar():
    print(f"We have credited {myslider2.get()} dollars to your bank account")
    tmsg.showinfo("Amount credited1 " f"We have credited {myslider2.get()} dollars to your bank account")
root=Tk()
root.geometry("755x555")
root.title("Slider")
Label(root,text="How many dollars do you want?").pack()
myslider2=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=10)
myslider2.set()
myslider2.pack()
Button(root,text="Get Dollars!",command=getdollar).pack()
root.mainloop()'''

# HOW TO MAKE A CALCULATOR

'''from tkinter import *
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())

        scvalue.set(value)
        screen.update()

    elif text == "c":
        scvalue.set("")
        screen.update()
    else :
        scvalue.set(scvalue.get()+text)
        screen.update()


root = Tk()
root.geometry("644x900")
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X)

f=Frame(root,bg="grey")
b=Button(f,text="9",font="lucida 30 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="8",font="lucida 30 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="7",font="lucida 30 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="6",font="lucida 30 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="5",font="lucida 30 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="4",font="lucida 30 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="3",font="lucida 30 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="2",font="lucida 30 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="1",font="lucida 30 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="0",font="lucida 30 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="+",font="lucida 30 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="-",font="lucida 30 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="*",font="lucida 30 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="/",font="lucida 30 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="%",font="lucida 30 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="=",font="lucida 30 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="c",font="lucida 30 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="//",font="lucida 30 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)


f.pack()
root.mainloop()'''

# PRACTICE SET OF OOP

'''class Students:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def display_info(self):
        print(f"The name is {self.name} and the age is {self.age} and the grade scored is {self.grade}")
student1=Students("Bhumika",18,"A+")
student1.display_info()'''

'''class Students:
    pass
obj1=Students()'''

class Staff:
    def __init__(self,name):
        self.name=name
class Teacher(Staff):
    def __init__(self,name,age):
        super().__init__(name)  
        self.age=age
obj1=Teacher("Bhumika",18)
print(obj1.name)
print(obj1.age)

        