"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    num = 1
    while len(list) < number_of_primes:
        flag = True
        for i in range(1, num):
            if(num % i ==0):
                flag = False
        if(flag):
            list.append(num)
        num += 1
    return list
