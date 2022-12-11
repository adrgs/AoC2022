def solve(lines):
    ans = 0
    priority = lambda p: ord(p)-0x60 if p.islower() else ord(p)-0x40+26
    for line in lines:
        line = line.strip()
        l = len(line)//2
        p1, p2 = line[:l], line[l:]
        s1, s2 = set(p1), set(p2)
        for c in s1.intersection(s2):
            ans += priority(c)
    print(ans)

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()