def factor_recur(n):

    if not isinstance(n, int):
        raise ValueError("Cannot enter a float value")

    if n < 0:
        raise ValueError("Cannot calculate factorial of negative numbers")

    if isinstance(n, str):
        raise ValueError("Cannot enter non-numeric value")

    if n == 0 or n == 1:
        return 1

    return n * factor_recur(n - 1)


if __name__ == "__main__":
    pass
