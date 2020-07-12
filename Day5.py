#Ass1 Day5

def isPrime(num):
    if num > 1:
        for i in range(2,num):
            if num % i ==0:
                return False
        else:
                return True
fltrObj=filter(isPrime, range(1,2500))
print("Prime numbers between 1-2500:",list(fltrObj))


#Ass2 Day5

import string
isCapWord = lambda element : string.capwords(element,sep=None)
myList = ["hey this is omkar","i am in omerga","....."]
newlist = list(map(isCapWord,myList))
print(newlist)
