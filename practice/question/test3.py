def print_formatted(number):
    Max = len(str(bin(number))[2:])
    for i in range(1, number + 1):
        o = oct(i)[2:]
        h = (hex(i)[2:]).upper()
        b = toBinary(i)
        print(str(i).rjust(Max), str(o).rjust(Max), str(h).rjust(Max), str(b).rjust(Max), sep=" ")

    # your code goes here


def toBinary(n):
    return (toBinary(n // 2) if n > 1 else '') + str(n % 2)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)