

# find d value which is private key
def find_d(e, t):
	# t = 60 , e = 13
	ee = float(e)
	tt = float(t)
	i = 1
	while True:
		rst = (i*tt+1)/ee
		print rst
		if rst.is_integer() == True:
			print "found whole value"
			return rst
		i += 1

# check if n is prime number or not
def is_prime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

# get totient value
def gen_totient():
	print "Function to get the totient"
	# get prime number with validation
	val1, val2 = input("Give me two prime numbers (commas between the values): ")
	# for i in range(min_val, max_val):
	while True:
		if is_prime(val1) == False:
			print "The first value is NOT prime number. Try again."
			val1 = input("Give me first prime number: ")
		else:
			break

	while True:
		if is_prime(val2) == False:
			print "The second value is NOT prime number. Try again."
			val2 = input("Give me second prime number: ")
		else:
			break

	# calculate totient
	totient = (val1-1)*(val2-1)
	return totient

# get e value
def get_e(totient):
	print "Function to get e value"
	e = input("Give me a value (less than %d): " % totient)
	while True:
		if is_prime(e) == False:
			print "You gave me NOT prime number Try again"
			e = input("Give me a value (less than %d): " % totient)
		else:
			break

	# check if it is co-prime with totient

	# calculate the output
	result = find_d(e, totient)
	print "The result is", result


####################################################################################
# To calculate the output (if you know e and totient already), press 'c'
# If you want to generate input first and calculate the output, press 'g'
####################################################################################
def main():
	print "# To calculate the output (if you know e and totient already), press 'c'\n# If you want to generate input first and calculate the output, press 'g'"
	mode = raw_input("Calculate output, press (c) OR Generate input, press (g):")
	if mode == "c" or mode == "C":
		e = raw_input("Give me (e): ")
		t = raw_input("Give me (t): ") 
		rst = find_d(e, t)
		print "The result is", rst
	elif mode == "g" or mode =="G":
		totient = gen_totient()
		print totient
		e = get_e(totient)
		

if __name__ == '__main__':
	main()