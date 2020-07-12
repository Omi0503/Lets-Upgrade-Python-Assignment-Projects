#Ass1 Day6

class Bank_Account: 
    def __init__(self): 
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ")
  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 
  
s = Bank_Account()
s.deposit() 
s.withdraw() 
s.display() 


#Ass2 Day6

import math
pi=math.pi
class Cone:
    def __init__(self,radius,height):
        self.r=radius
        self.h=height
    def surfacearea(self):
        return pi*self.r*(self.r+math.sqrt(self.h**2+self.r**2))
    def volume(self):
        return pi*self.r*self.r*self.h/3
b=Cone(5,12)
print("The surfacr area: ",b.surfacearea())
print("The volume: ",b.volume())
