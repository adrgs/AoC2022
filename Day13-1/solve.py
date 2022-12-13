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
                a[i] = [a[i]]
                order = cmp(a, b)
            elif type(b[i]) == int:
                b[i] = [b[i]]
                order = cmp(a, b)

        if order is not None:
            return order

        i += 1

def solve(lines):
    args = []
    ans = 0
    i = 1
    for line in lines:
        line = line.strip()
        if line:
            args.append(literal_eval(line))
        else:
            if cmp(*args):
                ans += i
            args = []
            i += 1
    if cmp(*args):
        ans += i

    print(ans)


def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()