def minOperations(n):
    if n == 1:
        return 0  # No operations needed for one 'H'
    
    operations = 0
    divisor = 2  # Start with the smallest divisor
    while n > 1:
        while n % divisor == 0:
            # If 'n' is divisible by the divisor, copy and paste 'divisor' times
            n //= divisor
            operations += divisor
        divisor += 1  # Move to the next divisor
    return operations