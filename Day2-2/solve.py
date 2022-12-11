def solve(lines):
    result = {'X': {'A':3, 'B':1, 'C':2}, 'Y': {'A':4, 'B':5, 'C':6}, 'Z': {'A':8, 'B':9, 'C':7}}
    ans = 0
    for line in lines:
        line = line.strip()
        if line:
            opp, us = line.split(' ')
            ans += result[us][opp]
    print(ans)

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()