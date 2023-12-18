

import re


def get_index_of_numbers(line):
    fptr = 0
    bptr = len(line) - 1
    i1, i2 = None, None
    while True:
        if fptr >= len(line):
            return None, None
        if i1 is None:
            v1 = line[fptr]
            if v1.isdigit():
                i1 = fptr
            fptr += 1
        if i2 is None:
            v2 = line[bptr]
            if v2.isdigit():
                i2 = bptr
            bptr -= 1

        if all([i1 is not None, i2 is not None]):
            break
    return i1, i2


with open("input.in", "r") as f:
    data = f.read().split("\n")


def p1():
    sum = 0
    for line in data:
        print(line)
        i1, i2 = get_index_of_numbers(line)
        joined = "".join([line[i1], line[i2]])
        print(joined)
        number = int(joined)
        sum += number

    print(sum)


# def p2():
#     numbers = ["one", "two", "three", "four",
#                "five", "six", "seven", "eight", "nine"]
#     sum = 0
#     for line in data:
#         i1, i2 = get_index_of_numbers(line)
#         found_indexes = []
#         for i, n in enumerate(numbers):
#             found_number = re.search(n, line)
#             if found_number:
#                 found_indexes.append([found_number.start(), i+1])

#         if i1 is not None:
#             found_indexes.extend([[i1, line[i1]], (i2, line[i2])])

#         result = sorted(found_indexes, key=lambda x: x[0])
#         number = f"{result[0][1]}{result[-1][1]}"
#         number = int(number)
#         sum += number
#     print(sum)


def p2():
    sum = 0
    for line in data:
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(int(c))

            for x, n in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                if line[i:].startswith(n):
                    digits.append(x)

        number = int(f"{digits[0]}{digits[-1]}")
        sum += number
    print(sum)


# p1()
p2()
