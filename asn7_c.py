import sys
from timeit import default_timer

start = 0

# check if it is the prime number, and returns co-prime value if it have
def prime(n):
	prime_list = []
	x = n
	print "Prime factors of %d are: " %x
	
	for i in range(1, x + 1):
		#All the factors of the number specified by the user
		if (x%i == 0):
			#Checks if it is a prime number and prints out only the prime numbers
			if(all(i % z for z in xrange(2, i))):
				#print (i)
				if i != 1:
					prime_list.append(i)
	
	return prime_list

# find d value which is private key
def find_d(e, t):
	# t = 60 , e = 13
	ee = float(e)
	tt = float(t)
	i = 1
	while True:
		rst = (i*tt+1)/ee
		#print rst
		if rst.is_integer() == True:
			return rst
		i += 1


def main():
	e, n = input("Give me value of e and n: ")
	prime_list = prime(n)
	#print prime_list

	# get p and q values
	p = prime_list[0]
	q = prime_list[1]

	# get totient value
	totient = (p-1)*(q-1)

	# get a "d" value
	rst = find_d(e, totient)

	# print "d" value
	print "Found whole value:", rst

	# print timer
	duration = default_timer() - start
	print "Spent time:", duration



if __name__ == '__main__':
	# start timer
	start = default_timer()
	main()