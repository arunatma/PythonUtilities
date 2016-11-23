# http://en.wikipedia.org/wiki/Twin_prime
# 4 * ( (m - 1)! + 1) mod m*(m+2) == -m mod m*(m+2)

def factorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Prints the series of mean of the twin primes till N
def get_twin_prime_means_till(N):
    mean_twin_primes = list()
    for m in range(2, N):
        divisor = m * (m + 2)
        lhs = (4 * (factorial (m - 1) + 1)) % divisor
        rhs = -m % divisor
        if lhs == rhs:
            mean_twin_primes.append(m + 1)
    return mean_twin_primes

def get_first_n_twin_prime_means(n):
    # Works till the value of 1000000
    mean_twin_primes = list()
    count = 0
    for m in range(2, 1000000):
        divisor = m * (m + 2)
        lhs = (4 * (factorial (m - 1) + 1)) % divisor
        rhs = -m % divisor
        if lhs == rhs:
            count += 1
            mean_twin_primes.append(m + 1)
        if count == n:
            break
    return mean_twin_primes
    
def get_nth_twin_prime_mean(n):
    # Works till the value of 1000000
    count = 0
    for m in range(2, 1000000):
        divisor = m * (m + 2)
        lhs = (4 * (factorial (m - 1) + 1)) % divisor
        rhs = -m % divisor
        if lhs == rhs:
            count += 1
        if count == n:
            return (m + 1)
