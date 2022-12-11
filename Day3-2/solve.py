def solve(lines):
    ans = 0
    priority = lambda p: ord(p)-0x60 if p.islower() else ord(p)-0x40+26
    for i in range(0, len(lines), 3):
        l1, l2, l3 = lines[i].strip(), lines[i+1].strip(), lines[i+2].strip()
        s1, s2, s3 = set(l1), set(l2), set(l3)
        for c in s1.intersection(s2).intersection(s3):
            ans += priority(c)
    print(ans)

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()