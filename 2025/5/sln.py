
def valid_ingredient(val: int, intervals: list[tuple[int, int]]) -> bool:
    for item in intervals:
        if item[0] <= val <= item[1]:
            return True
    return False

def merge_intervals(first: tuple[int, int], second: tuple[int, int]) -> tuple[int, int]:
    return min(first[0], second[0]), max(first[1], second[1])

def mergable_intervals(first: tuple[int, int], second: tuple[int, int]) -> bool:
    if ((first[0] >= second[0] and first[0] <= second[1]) or (first[1] >= second[0] and first[1] <= second[1]) or
            (second[0] >= first[0] and second[0] <= first[1]) or (second[1] >= first[0]) and second[1] <= first[1]):
        return True
    return False


def add_new_interval(val: tuple[int, int], intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    new_intervals = []
    for old_int in intervals:
        if mergable_intervals(val, old_int):
            val = merge_intervals(val, old_int)
        else:
            new_intervals.append(old_int)
    new_intervals.append(val)
    return sorted(new_intervals, key=lambda x: x[0])


def main():
    intervals = []
    fresh = 0
    with open('in.txt') as f:
        for line in f:
            if '-' in line:
                interval = line.split('-')
                intervals = add_new_interval((int(interval[0]), int(interval[1])), intervals)
            else:
                if line == '' or line == '\n':
                    continue
                if valid_ingredient(int(line.rstrip()), intervals):
                    fresh += 1
    print(fresh)


# need to first construct a list of intervals, merging when necessary
# then just go through the list of numbers and find what works.

if __name__ == '__main__':
    main()