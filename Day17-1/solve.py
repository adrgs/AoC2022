shapes = [
    [
     ['@','@','@','@'],
    ],
    [
     ['.','@','.'],
     ['@','@','@'],
     ['.','@','.'],
    ],
    [
     ['@','@','@'],
     ['.','.','@'],
     ['.','.','@'],
    ],
    [['@'],
     ['@'],
     ['@'],
     ['@'],
    ],
    [
     ['@','@'],
     ['@','@'],
    ],
]

def get_rindex(l, v):
    for i in range(len(l)-1, -1, -1):
        if l[i] == v:
            return i
    return None

def solve(lines):
    pattern = ''

    for line in lines:
        line = line.strip()
        if line:
            pattern = line

    width = 7
    j = 0

    board = []
    for i in range(2022):
        shape = shapes[i%len(shapes)]
        if len(board) == 0:
            for _ in range(3):
                board.append(['.'] * width)
        else:
            while '#' not in board[-4]:
                board.pop()
            if '#' in board[-1]:
                it = 3
            elif '#' in board[-2]:
                it = 2
            elif '#' in board[-3]:
                it = 1
            else:
                it = 0
            for _ in range(it):
                board.append(['.'] * width)

        # add shape to board
        for line in shape:
            board.append(['.'] * 2 + line + ['.'] * (width - len(line) - 2))

        while True:
            # move based on pattern
            p = pattern[j%len(pattern)]
            j += 1
            can_move = True
            for b in board:
                if '@' in b:
                    if p == '>':
                        idx = get_rindex(b, '@')
                        if idx == width - 1 or b[idx + 1] == '#':
                            can_move = False
                            break
                    elif p == '<':
                        idx = b.index('@')
                        if idx == 0 or b[idx - 1] == '#':
                            can_move = False
                            break
                    else:
                        raise ValueError('Invalid pattern')

            if can_move:
                if p == '>':
                    for b in board:
                        if '@' in b:
                            for k in range(len(b)-2, -1, -1):
                                if b[k] == '@':
                                    b[k + 1] = '@'
                                    b[k] = '.'
                elif p == '<':
                    for b in board:
                        if '@' in b:
                            for k in range(1, len(b)):
                                if b[k] == '@':
                                    b[k - 1] = '@'
                                    b[k] = '.'
                else:
                    raise ValueError('Invalid pattern')

            # move down
            can_move = not ('@' in board[0])
            if can_move:
                for k in range(len(board)-1):
                    if '@' in board[k+1]:
                        for t in range(width):
                            if board[k+1][t] == '@' and board[k][t] == '#':
                                can_move = False
                                break
                    if not can_move:
                        break
            
            if can_move:
                for k in range(len(board)-1):
                    for t in range(width):
                        if board[k+1][t] == '@':
                            board[k][t] = '@'
                            board[k+1][t] = '.'
            else:
                for k in range(len(board)):
                    for t in range(width):
                        if board[k][t] == '@':
                            board[k][t] = '#'

            if not can_move:
                break

    while '#' not in board[-1]:
        board.pop()

    print(len(board))

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()