'''Optional Assignment: Foo and Bar
Write a program that prints all the prime numbers and all the perfect squares
for all numbers between 100 and 100000.

For all numbers between 100 and 100000 test that number for whether it is 
prime or a perfect square. If it is a prime number print "Foo". If it is 
a perfect square print "Bar". If it is neither print "FooBar". Do not use 
the python math library for this exercise. For example, if the number you 
are evaluating is 25, you will have to figure out if it is a perfect square. It is, so print "Bar".

This assignment is extra challenging! Try pair programming and pulling up 
a white board.'''

def primality_check(min, max):
    for num in range(min, max+1):
        for divisor in range(2, num/2):
            if divisor*divisor == num:
                print num
                print "bar"
                break
            elif num % divisor == 0:
                print "foo"
                break
        print "foobar"
            # #     print "Foo"
            # #     break
            # print divisor**2
            # if (divisor**2) == num:
            #     print divisor**2
            #     print "Bar"
            #     break
            # else:
            #     print "FooBar"
            #     break
primality_check(100, 150)