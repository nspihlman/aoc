
def valid_coordinates(row, col, mp):
    return 0 <= row < len(mp) and 0 <= col < len(mp[row])


def is_paper_roll(row, col, mp):
    return mp[row][col] == '@' or mp[row][col] == 'x'


def check_neighbor_rolls(row: int, col: int, mp: list[str]) -> bool:
    # check if total neighbor rolls is < 4
    total = 0
    trsnfrms = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0,1),
                (1, -1), (1, 0), (1, 1)]
    for x in trsnfrms:
        chk_row = row+x[0]
        chk_col = col+x[1]
        if valid_coordinates(chk_row, chk_col, mp) and is_paper_roll(chk_row, chk_col, mp):
            total += 1
    return total < 4


def mark_for_change(row, col, mp):
    mp[row] = mp[row][:col] + 'x' + mp[row][col+1:]


def remove_marked_rolls(mp):
    for row in range(len(mp)):
        for col in range(len(mp[row])):
            if mp[row][col] == 'x':
                mp[row] = mp[row][:col] + '.' + mp[row][col+1:]


def find_accessible_rolls(mp: list[str]) -> int:
    total = 0
    while True:
        removed = 0
        for row in range(len(mp)):
            for col in range(len(mp[row])):
                if is_paper_roll(row, col, mp) and check_neighbor_rolls(row, col, mp):
                    removed += 1
                    mark_for_change(row, col, mp)
        if removed == 0:
            break
        total += removed
        remove_marked_rolls(mp)
    return total

def main():
    mp = []
    with open('in.txt') as f:
        for line in f:
            mp.append(line.rstrip())
    total_rolls = find_accessible_rolls(mp)
    print(total_rolls)

if __name__ == '__main__':
    main()