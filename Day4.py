#Ass1 Day4

def fib(num):
    x=0
    y=1
    while y < num:
        print(x)
        temp=y
        y=x+y
        x=temp
    return x
print(fib(int(input("Enter the number :- "))))


#Ass2 Day4

file = open("Binary.txt","w")
file.write("I love LetsUpgrade.")
file.close()

file = open("Binary.txt","r")
print(file.read())
file.close()

file = open("Binary.txt","a")
file.write("We all love Python Classes with LU")
file.close()

with open("Binary.txt","r") as file:
    print(file.read())


#Ass3 Day4

import random

def movies(*names):
	result=random.sample(names,2)
	print("recomded movies are:",' , '.join(result))
	
movie_type=input("enter movie type:-")
if movie_type=="action":
	movies('Logan','Avengers: Endgame','Mission: Impossible','The 39 Steps','The Terminator','X-Men: Days of Future Past')
	print(movies)
elif movie_type=="animation":
	movies('Spirited Away','Zootopia','Inside Out','Coco',' Paddington 2','Up')
	print(movies)
elif movie_type=="thrillers":
	movies('Frequency','Chasing Sleep','Session 9','Chinatown','The Third Man','Touch of Evil')
	print(movies)
elif movie_type=="drama":
	movies('Les Diaboliques','Zodiac','Mulholland Drive','Taxi Driver','Seven','The Conversation ')
	print(movies)
elif movie_type=="romcom":
	movies('Her','Always Be My Maybe','Chasing Amy','As Good As It Gets','Shes All That','Funny Face')
	print(movies)
else:
	print("sorry.wrong movie type")
