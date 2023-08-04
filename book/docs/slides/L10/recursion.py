def count_backward(number):
    """Recursive function for counting backwards."""
    print(number)
    if number > 1:
        count_backward(number - 1)


def count_forward(number):
    """Recursive function for counting forward."""
    if number > 1:
        count_forward(number - 1)
    print(number)


def fac(n):
    """Factorial."""
    print(f"Computing {n}!.")
    if n <= 1:
        return 1
    return fac(n - 1) * n


def fib(n):
    """Fibonacci."""
    print(f"Computing fib({n}).")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
