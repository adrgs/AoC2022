def solve(lines):
    cycle = 0
    X = 1
    ans = 0

    def check():
        nonlocal ans
        if cycle == 20 or (cycle-20)%40 == 0:
            ans += X * cycle

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
    
    print(ans)

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()