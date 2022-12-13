from ast import literal_eval

def cmp(a, b):
    i = 0
    while True:
        if i == len(a) and i == len(b):
            return None
        elif i == len(a):
            return True
        elif i == len(b):
            return False

        order = None
        if type(a[i]) == type(b[i]):
            if type(a[i]) == int:
                if a[i] > b[i]:
                    order = False
                elif a[i] < b[i]:
                    order = True
                else:
                    order = None
            elif type(a[i]) == list:
                order = cmp(a[i], b[i])
        else:
            if type(a[i]) == int:
                l = list(a)
                l[i] = [l[i]]
                order = cmp(l, b)
            elif type(b[i]) == int:
                l = list(b)
                l[i] = [l[i]]
                order = cmp(a, l)

        if order is not None:
            return order

        i += 1

def solve(lines):
    packets = []
    for line in lines:
        line = line.strip()
        if line:
            packets.append(literal_eval(line))

    packets.append([[2]])
    packets.append([[6]])

    for i in range(len(packets)):
        for j in range(i + 1, len(packets)):
            if not cmp(packets[i], packets[j]):
                packets[i], packets[j] = packets[j], packets[i]

    a, b = packets.index([[2]])+1, packets.index([[6]])+1

    print(a*b)

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()