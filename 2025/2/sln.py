
def check_interval(start: int, end: int) -> int:
    total = 0
    for num in range(start, end+1):
        num_str = str(num)
        substr = ""
        for val in num_str:
            substr = substr + val
            if len(substr) > (len(num_str) / 2 + 1) or len(substr) == len(num_str):
                break
            if len(num_str) % len(substr) == 0:
                mult = len(num_str) // len(substr)
                if (substr * mult) == num_str:
                    print(f"{substr} for {num_str}")
                    total += num
                    break
    return total

def main():
    ranges = []
    total = 0
    with open('in.txt') as f:
        for line in f:
            ranges = line.split(',')
    for r in ranges:
        range_vals = r.split('-')
        total += check_interval(int(range_vals[0]), int(range_vals[1]))
    print(total)



if __name__ == '__main__':
    main()