#Ass1 Day3
alt = int(input("Enter the current altitude "))
if alt >=5000:
   print("Turn around")
elif alt > 1000 and alt < 5000:
   print("Bring down to 1000")
elif alt == 1000:
   print("Safe to land")
#Ass2 Day3
print("Prime numbers between the range(1,200) are:")
for num in range(1, 200 + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
#Ass3 Day3
print("first armstrong numbers in the range(1042000,702648265):")
for num in range(1042000,702648265):
    sum=0
    temp=num
    while temp> 0:
        i=temp % 10
        sum += (i**7)
        temp = temp // 10
    if sum == num:
        print("The first armstrong number is",num)
        break
