#!/usr/bin/env python3
"""Fibonacci Sequence Calculator - First 15 numbers"""

def fibonacci(n):
    """Generate Fibonacci sequence up to n numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Calculate first 15 Fibonacci numbers
result = fibonacci(15)

# Display results
print("First 15 Fibonacci numbers:")
for i, num in enumerate(result, 1):
    print(f"  {i:2}. {num}")
