def factor_recur(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: Factorial of the input integer.

    Raises:
    ValueError: If `n` is not a non-negative integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be non-negative integer")

    if n == 0 or n == 1:
        return 1

    return n * factor_recur(n - 1)


if __name__ == "__main__":
    pass
