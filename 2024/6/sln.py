import sys
def travel_up(map: list[list[str]], row: int, col: int, total: list[int]):
    if map[row][col] != 'X':
        total[0] += 1
        map[row][col] = 'X'

    if row == 0:
        return total[0]
    elif map[row-1][col] == '#':
        return travel_right(map, row, col, total)
    return travel_up(map, row-1, col, total)

def travel_down(map: list[list[str]], row: int, col: int, total: list[int]):
    if map[row][col] != 'X':
        total[0] += 1
        map[row][col] = 'X'

    if row == (len(map) - 1):
        return total[0]
    elif map[row+1][col] == '#':
        return travel_left(map, row, col, total)
    return travel_down(map, row+1, col, total)

def travel_right(map: list[list[str]], row: int, col: int, total: list[int]):
    if map[row][col] != 'X':
        total[0] += 1
        map[row][col] = 'X'

    if col == (len(map[row])-1):
        return total[0]
    elif map[row][col+1] == '#':
        return travel_down(map, row, col, total)
    return travel_right(map, row, col+1, total)

def travel_left(map: list[list[str]], row: int, col: int, total: list[int]):
    if map[row][col] != 'X':
        total[0] += 1
        map[row][col] = 'X'

    if col == 0:
        return total[0]
    elif map[row][col-1] == '#':
        return travel_up(map, row, col, total)
    return travel_left(map, row, col-1, total)

def track_guard(map: list[list[str]]):
    total = [1]
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == '<':
                map[row][col] = 'X'
                return travel_left(map, row, col, total)
            if map[row][col] == '>':
                map[row][col] = 'X'
                return travel_right(map, row, col, total)
            if map[row][col] == '^':
                map[row][col] = 'X'
                return travel_up(map, row, col, total)
            if map[row][col] == 'v':
                map[row][col] = 'X'
                return travel_down(map, row, col, total)
    return total

# i got 129/130 and it was too low


def main():
    map: list[list[str]] = []
    sys.setrecursionlimit(12000)
    with open("/Users/nicholasspihlman/code/aoc/2024/6/in.txt") as f:
        for line in f:
            vars = []
            line = line.rstrip()
            for item in line:
                vars.append(item)
            map.append(vars)
    print(track_guard(map))
            

if __name__ == '__main__':
    main()