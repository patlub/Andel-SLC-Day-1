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
