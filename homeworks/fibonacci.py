import pytest


def fibonacci(n, stack=[]):
    if n <= 1:
        return n

    stack.append(n - 1)
    a1 = fibonacci(n - 1, stack)
    stack[-1] = {n - 1: a1}
    print(stack)

    stack.append(n - 2)
    a2 = fibonacci(n - 2, stack)
    stack[-1] = {n - 2: a2}
    print(stack)
    stack.pop()
    stack.pop()

    return a1 + a2


if __name__ == "__main__":
    fibonacci(9)
