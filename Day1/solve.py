def solve(lines):
    elves = [0]
    for line in lines:
        line = line.strip()
        if line:
            elves[-1] += int(line)
        else:
            elves.append(0)
    print(max(elves))

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()