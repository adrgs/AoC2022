class Interval:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def fully_contains(self, other):
        return self.start <= other.start and other.end <= self.end

    def overlaps(self, other):
        return (self.start <= other.start <= self.end) or (other.start <= self.start <= other.end)


def solve(lines):
    ans = 0
    for line in lines:
        line = line.strip()
        if line:
            p1, p2 = line.split(',')
            i1, i2 = Interval(*map(int, p1.split('-'))), Interval(*map(int, p2.split('-')))

            ans += i1.overlaps(i2)
    print(ans)

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()