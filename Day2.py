#python data structure
#list
lst=[1,3.4,"omkar",'a']
print(lst)
#methods of data structure list
lst.append("omi")
print(lst)
lst.insert(1,"ravan")
print(lst)
lst.remove("a")
print(lst)
lst.pop(0)
print(lst)
del lst
print("now list is empty")

#Dictionary
thisdict={"brand":"bmw","model":"xm","year":"2020"}
print(thisdict)
x=thisdict.get("model")
print(x)
thisdict["year"]=2018
print(thisdict)

#set
thisset={"name","rollno","bod"}
print(thisset)
#to access item in set
print("rollno" in thisset)
#add item in set
thisset.add("class")
print(thisset)
# to update set
thisset.update(["man","women","boy"])
print(thisset)
#get no of items in set
print(len(thisset))
#remove item from set
thisset.remove("man")
print(thisset)
#discrad methode
thisset.discard("women")
print(thisset)
#to empty set
thisset.clear()
print(thisset)
#union to add another set in previos
set1={1,2,3}
set2={'a','v','d'}
set3=set1.union(set2)
print(set3)

#tuples
thistuple=("bro","friend","son")
print(thistuple)
#to access item
print(thistuple[1])
#print range elements
print(thistuple[1:2])
#change tuple value
x=('a','c','b')
y=list(x)
y[1]="aashu"
x=tuple(y)
print(x)
#print length of tuple
print(len(thistuple))
#delete item from tuple
del thistuple
print("there is no item in tuple")
#count
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)
#index
x = thistuple.index(8)
print(x)

#string
print("hello")
#string methods
#strip
a="Hello,World"
print(a.strip())
#lower
print(a.lower())
#upper
print(a.upper())
#replace
print(a.replace("h","r"))
#split
print(a.split(","))
#format
age = 21
txt = "My name is omkar, and I am {}"
print(txt.format(age))
