import time

def generate_primes(n) -> list:
    """
    Function to generate prime numbers form 0 to n
    Args:
        n: Upper limit for generating prime numbers
    Raises:
        TypeError: If argument is not an integer
    Returns:
         list: A list of the generated prime numbers
    """
    if not isinstance(n, int):
        raise TypeError('Argument should be an integer')

    elif n < 2:
        return []

    # Start Timer
    start = time.time()

    # initialize list to hold prime numbers
    primes = []
    for num in range(2, n + 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)

    end = time.time()
    print("The program ran for " + str(end-start))
    return primes


generate_primes(10) # The program ran for 0.0
generate_primes(100) # The program ran for 0.0
generate_primes(1000) # The program ran for 0.0010271072387695312
generate_primes(10000) # The program ran for 0.8187892436981201

# Running time is O(n). Linear Running time