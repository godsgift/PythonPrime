import sys
from timeit import default_timer

def prime():
	x = int(input("Enter your number: "))
	print "Prime factors of %d are: " %x
	start = default_timer()
	for i in range(1, x + 1):
		#All the factors of the number specified by the user
		if (x%i == 0):
			#Checks if it is a prime number and prints out only the prime numbers
			if(all(i % z for z in xrange(2, i))):
				print (i)
	duration = default_timer() - start
	print duration
prime()