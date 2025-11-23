# Fibonacci numbers

a, b = 0, 1          # Start with the first two Fibonacci numbers
while a < 1000:      # Continue until a reaches or exceeds 1000
    print(a, end=',')  # Print current number followed by a comma (no newline)
    a, b = b, a + b    # Move to next pair: a becomes b, b becomes a+b