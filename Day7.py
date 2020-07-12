#Ass1 Day7

file = open("FF.txt","w")
file.close()

file = open("FF.txt","r")
try:
    file.write("Hi Guys")
except Exception as e:
    print("There was an error in the file handling")
    print("Error was -",e)
finally:
    file.close()

print("Hey guys,rate the session as of right now")

#Ass2 Day7
#unit test code

import unittest
from m import *


class TestPrime(unittest.TestCase):

    def test_prime(self):
        self.assertAlmostEqual(prime(a),True)



    def test_values(self):
        self.assertRaises(ValueError,prime,-2)
    def test_types(self):
        self.assertRaises(TypeError,prime,'a')
        self.assertRaises(TypeError, prime, True)
        self.assertRaises(TypeError, prime, 3+5j)

#Ass2 Day7
#function code

def prime(a):
    if(a<0):
        raise ValueError("The no is negative")
    if type(a) not in [int]:
        raise TypeError("Insert Only Integer Value ")
    else:
        c = 0
        for i in range(1, a + 1):
            if (a % i == 0):
                c = c + 1
        if (c == 2):
            return True

        else:
            return False




a=int(input("Enter a  no\n"))
prime(a)
