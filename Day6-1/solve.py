def solve(lines):
    for line in lines:
        line = line.strip()
        if line:
            for i in range(4, len(line)):
                if len(set(line[i-4:i])) == 4:
                    print(i)
                    break
    

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()