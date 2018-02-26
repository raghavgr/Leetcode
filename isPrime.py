def isPrime(num):
    if num == 2 or num == 3: return True
    if num % 2 ==0 or num < 2: return False
    if num > 3:
        for i in range(1, int(num**0.5) + 1, 2):    # only odd numbers
            if num % i == 0:
                return False
    
    return True

print(isPrime(9))