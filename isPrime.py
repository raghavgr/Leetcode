def isPrime(self, num):
    if num== 2 or num == 3: return True
    if num%2==0 or num<2: return False
    for i in range(3, int(num**0.5), 2):    # only odd numbers
        if num%i == 0:
            return False
    
    return True