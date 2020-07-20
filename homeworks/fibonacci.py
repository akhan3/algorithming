#!/usr/bin/env python3


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_call_stack(n, stack=None):
    if stack is None:  # https://stackoverflow.com/a/113198/107349
        stack = list()
    if n <= 1:
        return n

    stack.append(n - 1)
    a1 = fibonacci_call_stack(n - 1, stack)
    stack[-1] = {n - 1: a1}
    print(stack)

    stack.append(n - 2)
    a2 = fibonacci_call_stack(n - 2, stack)
    stack[-1] = {n - 2: a2}
    print(stack)
    stack.pop()
    stack.pop()

    return a1 + a2


if __name__ == "__main__":
    x = 7
    print(fibonacci(x))
    fibonacci_call_stack(x)
