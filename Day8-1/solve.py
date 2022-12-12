def visible(grid, i, j):
    m, n = len(grid), len(grid[0])
    if i == 0 or j == 0 or i == m-1 or j == n-1:
        return True

    invis = 0

    ip = i
    while ip > 0:
        ip -= 1
        if grid[ip][j] >= grid[i][j]:
            invis += 1
            break
    ip = i
    while ip < m-1:
        ip += 1
        if grid[ip][j] >= grid[i][j]:
            invis += 1
            break
    
    ij = j
    while ij > 0:
        ij -= 1
        if grid[i][ij] >= grid[i][j]:
            invis += 1
            break

    ij = j
    while ij < n-1:
        ij += 1
        if grid[i][ij] >= grid[i][j]:
            invis += 1
            break

    if invis == 4:
        return False
    return True

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
            if visible(grid, i, j):
                ans += 1
    
    print(ans)

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()