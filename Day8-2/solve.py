def score(grid, i, j):
    m, n = len(grid), len(grid[0])
    if i == 0 or j == 0 or i == m-1 or j == n-1:
        return 0

    s = 1

    ip = i
    while ip > 0:
        ip -= 1
        if grid[ip][j] >= grid[i][j]:
            break

    s *= (i - ip)
    
    ip = i
    while ip < m-1:
        ip += 1
        if grid[ip][j] >= grid[i][j]:
            break

    s *= (ip - i)
    
    ij = j
    while ij > 0:
        ij -= 1
        if grid[i][ij] >= grid[i][j]:
            break

    s *= (j - ij)

    ij = j
    while ij < n-1:
        ij += 1
        if grid[i][ij] >= grid[i][j]:
            break

    s *= (ij - j)

    return s

def solve(lines):
    grid = []
    for line in lines:
        line = line.strip()
        if line:
            grid.append([int(x) for x in list(line)])

    ans = 0
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            ans = max(ans, score(grid, i, j))
    
    print(ans)

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()