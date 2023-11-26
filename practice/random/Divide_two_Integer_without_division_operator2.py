def divide_without_division_operator(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero")

    # Determine the sign of the result
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

    # Take the absolute values of dividend and divisor
    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0
    while dividend >= divisor:
        temp_divisor, temp_quotient = divisor, 1

        # Double the divisor until it's greater than the remaining dividend
        while dividend >= temp_divisor:
            dividend -= temp_divisor
            quotient += temp_quotient

            # Double the divisor and the quotient
            temp_divisor <<= 1
            temp_quotient <<= 1

    # Apply the sign to the result
    quotient *= sign

    return quotient, dividend  # Return quotient and remainder

# Example usage:
dividend = 47
divisor = 4
result, remainder = divide_without_division_operator(dividend, divisor)
print("Quotient:", result)
print("Remainder:", remainder)
