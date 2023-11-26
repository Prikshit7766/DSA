def divide_without_division_operator(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero")

    # Determine the sign of the result
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

    # Take the absolute values of dividend and divisor
    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    # Apply the sign to the result
    quotient *= sign

    return quotient

# Example usage:
dividend = 20
divisor = 3
result = divide_without_division_operator(dividend, divisor)
print("Quotient:", result)
