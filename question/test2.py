import textwrap
def wrap(string, max_width):
    l = len(string)
    c = max_width

    if l // max_width != 0:
        count = 0
        for i in range(l // max_width):
            print(string[count:max_width])
            count = count + c
            max_width += c
    if l % c != 0:
        return (string[-(l % c):])

    return




if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)