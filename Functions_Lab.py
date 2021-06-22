#**********************
# Functions
#********************

# Functions = Repetative/Reuse = Write once and use multiple times.
# Return a value / keep the value
# Anonymous functions = functions without a name = functions as argument to other functions= lambda
# One line short functions/Multiple Arguments/Nested functions
#Built in functions/User defined functions

print("Welcome to Python!"); # print() = Is a built in function.

#Simple function
def great():
print("welcome to Python!")

great()  # gives "welcome to Python!"

foo = lambday: 4*y 
print(foo(3)) * # gives 12

#function with arguments
def my_house(brookbond, taj):
    lipton=0
    lipton += 1
    brookbond = taj + lipton
print(brookbond)
nescafe = 0
my_house(1,2) # gives 3

# data inside the function is in local scope, we can't access directly from out side of the funciton.
# data outside the funciton is in global scope, we can access directly from any where.

def my_house():
    global nescafe          # define the nescafe object as global
    nescafe = 'Latte'       # assign a new value to the nescafe object -> nescafe value changed from 0 to 'Latte'
    print(nescafe)
my_house() # gives 'Latte'

#Parameter Passing
def sumNums(n1,n2,n3):
    sum = n1+n2+n3
    return sum  # or you can write it as -> print(sum) -> both give same results
sumNums(1,2,3)  # gives 1+2+3 = 6

def sumNums(n1, n2=20, n3=30):      #Here n1 is a positional argument & n2,n3 are default arguments
    sum = n1+n2+n3
    return sum
sumNums(1)  # which consider n1=1,n2=20,n3=30 -> gives 1+20+30 = 51
sumNums(10,100)     # which consider n1=10,n2=100,n3=30 -> gives 10+100+30 = 140

tea = sumNums(10,100) # you can access the function outside with a new object
tea # gives 140 -> Is get value only when you have return in the function.

tot = sumNums(n3=10,n2=30,n1=50) # Here n1,n2,n3 are named arguments
tot # gives 50+30+10 = 90 
tot = sumNums(10,30,50) # If you don't give the argumentname with assigment then the function consider in an order(n1=10,n2=30,n3=50).

#*******************************
def f1(taj):
    brookbond = 0
    brookbond = brookbond + taj
    return brookbond
f1(10)  # gives you 10

def f2(taj,tatatea):
    brookbond = 0
    brookbond = brookbond + taj + tatatea
    return brookbond
f2(1,2) # gives you 3

def f3(taj,tatatea,chakra):
    brookbond = 0
    brookbond = brookbond + taj + tatatea + chakra
    return brookbond
f(1,2,3)    # gives you 6

def f100(taj,tatatea,chakra,....tea100):    # invalid function declaration
    brookbond = 0
    brookbond = brookbond + taj + tatatea + chakra + ....100
    return brookbond
f100(1,2,3,...100)      # invalid function declaration


def f( *tray ):     # single argument, which fulfills a call with any no of arguments. -> expecting list of object 
    tea = 0         # Eg:-It looks like cups are not going inside the house, whole tray with n no of cups going inside house.
    for cup in tray:
        tea = tea + cup
        return tea
f(1)    # gives 1
f(1,3)  # gives 3
f(1,2,3)    # gives 6        

def fruitBasket( **kvargs ):    # expecting a dictionary
    count = 0
    for key,val in kvargs.items():
        printString = "{:20}{:10}".format(key,val)
        print(printString)
        count = count + val 
    return count
    
tot = fruitBasket(apples=100,banana=144,pears=77,grapes=200,mangoes=35)
print("-" * 30)
print( "{:20}{:10}".format("Total Fruits: ", tot))

def myFunc( n1,n2,n3, *args, **kvargs ):    #n1,n2,n3 = positional arguments 
    sum1 = sum2 + sum3 = 0                  # *args = variable number of arguments
    sum1 = n1 + n2 + n3                     #**kvargs = keyvalue arguments
    for n in args:
        sum2 = sum2 + n
    for k.v in kvargs.items():
        sum3 = sum3 + v
    sums = [sum1, sum2, sum3]
    return sums
sums = myFunc(10,20,30,11,22,33,44,one=100,two=200,three=300)
print(sums)


# Classes
#******************

class Person(): # Empty class, like empty architecture plan
    pass

sachin = Person()   # sachin is an object of Person class

class Person():
    def __init__(self): # It is a constructor. It is being called by Python at the time of constructing an object, so we call it as a constructor.
    print("I am in Constructor") 
sachin = Person()   # sachin is an object, which calls the class Person() & gives "I am in Constructor"


class Person():
    def __init__(self,aName,anAge): # self is called self referencing variable, we no need to pass as parameter in the function.
        print("I am in Constructor")
        self.name = aName
        self.age = anAge
sachin = Person('Tendulkar',49)   # gives "I am in Constructor".
sachin.name # gives Tendulkar
sachin.age  # gives 49

dhoni = Person('Dhoni',35)   # gives "I am in Constructor".
dhoni.name  # gives Dhoni
dhoni.age   # gives 35

class CricketPlayer():
    def __init__(self,aName,aBat,aBall):
        print("I am in Constructor')
        self.name = aName
        self.bat = aBat
        self.ball = aBall
        
sachin = CricketPlayer('sachin','MRF','Guru')
sachin.name 
sachin.bat
sachin.ball 

class BadmintonPlayer():
    def __init__(self,aName,aRacket,ashuttle):
    print("I am in constructor")
    self.name = aName
    self.bat = aBat
    self.shuttle
sindhu = BadmintonPlayer('Sindhu','yonex','yonex')
sindhu.racket
sindhu.shuttle

class Person():
    def __init__(self,anName,anAge,aSal):
        print("I am in constructor")
        self.name = aName
        self.age = anAge
        self.salary = aSal
    def eat(self):
        print('Idly')
     
    def play(self):
        print('Badminton')
        print('or cricket')
    
    def excercise(self):
        print("Jogging')
        
sachin = Person('Tendulkar',49)
sachin.name
sachin.eat()       
sachin.play()
sachin.excercise()




























 
