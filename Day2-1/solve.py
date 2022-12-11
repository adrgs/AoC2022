def solve(lines):
    points = {'X': 1, 'Y': 2, 'Z': 3}
    result = {'X': {'A':3, 'B':0, 'C':6}, 'Y': {'A':6, 'B':3, 'C':0}, 'Z': {'A':0, 'B':6, 'C':3}}
    ans = 0
    for line in lines:
        line = line.strip()
        if line:
            opp, us = line.split(' ')
            ans += points[us] + result[us][opp]
    print(ans)

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()