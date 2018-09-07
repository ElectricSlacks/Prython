import math 
file = open('Primes.txt', 'w')


for num in range(1,30):     #to iterate between 10 to infinity
   for i in range(2,num):    #to iterate on the factors of the number
      if num%i == 0:         #to determine the first factor
         j=num/i             #to calculate the second factor
         
         break #to move to the next number, the #first FOR
      else:                  # else part of the loop
         file.write("str.num")
         file.write("\r\n")
file.close()

