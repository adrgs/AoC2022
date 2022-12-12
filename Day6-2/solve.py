def solve(lines):
    for line in lines:
        line = line.strip()
        if line:
            for i in range(14, len(line)):
                if len(set(line[i-14:i])) == 14:
                    print(i)
                    break
    

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()