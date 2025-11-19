import math

def is_calibrated(values: list[int], target: int, running_total: int) -> bool:
    totstr = str(running_total)
    righstr = str(values[0])
    newval = int(totstr+righstr)
    if len(values) == 1 and (((running_total*values[0]) == target) or ((running_total+values[0])==target) or newval == target):
        return True
    elif len(values) == 1:
        return False
    if newval <= target:
        return is_calibrated(values[1:], target, running_total*values[0]) or is_calibrated(values[1:], target, running_total+values[0]) or is_calibrated(values[1:], target, newval)
    elif (running_total * values[0]) <= target:
        return is_calibrated(values[1:], target, running_total*values[0]) or is_calibrated(values[1:], target, running_total+values[0])
    elif (running_total + values[0]) <= target:
        return is_calibrated(values[1:], target, running_total+values[0])
    return False
        

def main():
    all_input = []
    with open('/Users/nicholasspihlman/code/aoc/2024/7/in.txt') as f:
        for line in f:
            values = []
            total = int(line.split(':')[0])
            values.append(total)
            others = line.split(': ')[1].split(' ')
            for num in others:
                values.append(int(num))
            all_input.append(values)
    total = 0
    # got 932137703733, too low
    for line in all_input:
        if is_calibrated(line[2:], line[0], line[1]):
            total += line[0]
    print(total)
       


if __name__ == '__main__':
    main()