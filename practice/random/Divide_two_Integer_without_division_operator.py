
def divide_without_division_operator_approch1(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero")

    # Determine the sign of the result
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1  #xor operation 

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
result = divide_without_division_operator_approch1(dividend, divisor)
print("Quotient:", result)





def divide_without_division_operator_approch2(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero")

    # Determine the sign of the result
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

    # Take the absolute values of dividend and divisor
    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0
    while dividend >= divisor:
        temp_quotient = 1
        temp_divisor = divisor

        while dividend >= temp_divisor:
            temp_divisor <<= 1
            temp_quotient <<= 1

        # Adjust the dividend without using right shift
        dividend -= temp_divisor // 2
        quotient += temp_quotient // 2

    # Apply the sign to the result
    quotient *= sign

    return quotient, dividend  # Return quotient and remainder

# Example usage:
dividend = 47
divisor = 4
result, remainder = divide_without_division_operator_approch2(dividend, divisor)
print("Quotient:", result)
print("Remainder:", remainder)
