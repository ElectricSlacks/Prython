import math 
file = open('Primes.txt', 'w')
file.close()

for num in range(1,i):     #to iterate between 10 to infinity
   for i in range(2,num):    #to iterate on the factors of the number
      if num%i == 0:         #to determine the first factor
         j=num/i             #to calculate the second factor
         print '%d equals %d * %d' % (num,i,j)
         break #to move to the next number, the #first FOR
      else:                  # else part of the loop
         print num, 'is a prime number'

file = open("Primes.txt","w")
file.write(Primes)
file.write("\r\n")
file.close()
