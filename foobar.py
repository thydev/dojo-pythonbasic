# Write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000.

# For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square. 
# If it is a prime number, print "Foo". If it is a perfect square, print "Bar". 
# If it is neither, print "FooBar". Do not use the python math library for this exercise. For example, 
# if the number you are evaluating is 25, you will have to figure out if it is a perfect square. It is, so print "Bar".

def foobar(num_start = 100, num_end = 10000):
    for num in range(num_start, num_end+1):
        if isPrime(num):
            print "Foo", num
        elif isPerfectSquare(num):
            print "Bar", num
        else:
            print "FooBar", num

def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def isPerfectSquare(num):
    for i in range(1, int(num / 2)):
        if i * i == num:
            return True
    
    return False

print "Prime:", isPrime(5)
print "Perfect Square:", isPerfectSquare(9)
print "Perfect Square:", isPerfectSquare(91)
print "Perfect Square:", isPerfectSquare(100)

foobar()