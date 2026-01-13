
def split_beams(tmap: list[str]) -> int:
    tot_split = 0
    start_col = 0
    for c in range(len(tmap[0])):
        if tmap[0][c] == 'S':
            start_col = c

    tmap[1] = tmap[1][0:start_col] + "|" + tmap[1][start_col+1:]

    for i in range(1, len(tmap) - 1):
        new_bot_line, splits = compare_two_lines(tmap[i], tmap[i+1])
        tmap[i+1] = new_bot_line
        tot_split += splits
    return tot_split

def compare_two_lines(top_line: str, bot_line: str) -> tuple[str, int]:
    split = 0
    for i in range(len(top_line)):
        if top_line[i] == '|':
            if bot_line[i] == '^':
                bot_line = split_beam(bot_line, i)
                split += 1
            else:
                bot_line = bot_line[0:i] + '|' + bot_line[i+1:]
    return bot_line, split

def split_beam(line: str, idx: int) -> str:
    if idx == 0:
        return '^|' + line[2:]
    elif idx == len(line) - 1:
        return line[:idx-1] + '|^'
    else:
        return line[0:idx-1] + '|^|' + line[idx+2:]

def main():
    tmap = []
    with open('in.txt') as f:
        for line in f:
            tmap.append(line.rstrip())
    print(split_beams(tmap))


if __name__ == '__main__':
    main()