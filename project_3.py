"""
Problem 3
Large Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29

What is the largest prime factor of the number 600851475143 ?
"""

def largest_prime_factor(number):
    # Initialize variables
    i = 2
    factors = []

    # Factorize the number
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)

    if number > 1:
        factors.append(number)

    # Return the largest prime factor
    return (factors)

# Example for the number 600851475143
result = largest_prime_factor(600851475143)
print(result)
