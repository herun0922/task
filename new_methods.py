# new_methods.py

def fibonacci(n):
    """Compute the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
