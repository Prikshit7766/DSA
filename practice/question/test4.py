def merge_the_tools(string, k):
    l = wrap(string, k)

    for i in l:
        n = len(i)

        print(removeDuplicate(list(i)))


def removeDuplicate(str):
    p = ""
    for char in str:
        if char not in p:
            p = p + char
    return (p)

    # your code goes here


def wrap(string, max_width):
    l = len(string)
    c = max_width
    z = []

    if l // max_width != 0:
        count = 0
        for i in range(l // max_width):
            z.append(string[count:max_width])
            count = count + c
            max_width += c
    if l % c != 0:
        z.append(string[-(l % c):])
        return z

    return z


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)