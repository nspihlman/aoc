
def is_level_safe(rpt: list[int]) -> bool:
    asc: bool = False
    idx: int = 0
    while(idx < len(rpt) - 1):
        if (abs(rpt[idx] - rpt[idx+1]) > 3 or rpt[idx] == rpt[idx+1]):
            return False
        if idx == 0:
            if rpt[idx] < rpt[idx+1]:
                asc = True
        elif rpt[idx] < rpt[idx+1] and not asc:
            return False
        elif rpt[idx] > rpt[idx+1] and asc:
            return False
        idx += 1
    return True

def main():
    reports = []
    with open('reports.txt') as f:
        for line in f:
            line.rstrip()
            levels = line.split(' ')
            levels = [int(lvl) for lvl in levels]
            reports.append(levels)

    safelevels = 0
    for report in reports:
        if is_level_safe(report):
            safelevels += 1
        else:
            for idx in range(len(report)):
                temp = []
                for i in range(len(report)):
                    if i == idx:
                        continue
                    else:
                        temp.append(report[i])
                if is_level_safe(temp):
                    safelevels += 1
                    break
    print(safelevels)

if __name__ == '__main__':
    main()

