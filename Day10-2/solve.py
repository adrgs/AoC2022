def solve(lines):
    cycle = 0
    X = 1
    ans = 0
    i = 0

    def check():
        nonlocal ans
        nonlocal i
        if X-1 <= i <= X+1:
            print("#", end='')
        else:
            print(".", end='')
        i += 1
        if i == 40:
            print()
            i = 0

    for line in lines:
        line = line.strip()
        if line:
            if line == 'noop':
                cycle += 1
                check()
            else:
                addx, amount = line.split()
                amount = int(amount)
                cycle += 1
                check()
                cycle += 1
                check()
                X += amount

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()