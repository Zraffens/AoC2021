def result1(data: list, value: str) -> int:
    commons = []
    for column in bits_in_order(data):
        match value:
            case 'gamma':
                common = 1 if column.count('1') > column.count('0') else 0
            case 'epsilon':
                common = 0 if column.count('1') > column.count('0') else 1
        commons.append(common)
    commons = commons[0:12]
    return ''.join([str(i) for i in commons])


def result2(data: list, value: str) -> int:
    numbers_required = [[] for _ in range(12)]
    bits = bits_in_order(data)
    print(len(bits))
    for index, column in enumerate(bits):
        print(index)
        match value:
            case 'oxygen':
                common = 1 if column.count('1') > column.count('0') or column.count('1') == column.count('0') else 0
            case 'co2':
                common = 0 if column.count('1') > column.count('0') or column.count('1') == column.count('0') else 1
        for line in data:
            if int(line[index]) == int(common):
                numbers_required[index].append(line)

    print(numbers_required)


def bits_in_order(data):
    bits_in_order = ['' for i in range(len(data))]
    for line in data:
        for index, bit in enumerate(line):
            bits_in_order[index] += str(bit)

    return bits_in_order[:12]


with open('day3.txt') as f:
    data = f.readlines()


# print(result(data, 'gamma'))
# print(result(data, 'epsilon'))

print(result2(data, 'oxygen'))
