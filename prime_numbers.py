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

    primes = []
    for num in range(2, n + 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
    return primes
