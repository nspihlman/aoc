

def find_grand_total(nums: list[list[int]], ops: list[str]) -> int:
    total = 0
    for i in range(len(ops)):
        if ops[i] == '+':
            total += nums[0][i] + nums[1][i] + nums[2][i] + nums[3][i]
        else:
            total = total + (nums[0][i] * nums[1][i] * nums[2][i] * nums[3][i])
    return total

def main():
    lines = []
    operations = []
    with open('in.txt') as f:
        for line in f:
            line = line.lstrip().rstrip()
            line = line.split(' ')
            vals = [x for x in line if not x.isspace() and x != '']
            if vals[0][0].isdigit():
                lines.append([int(x) for x in vals])
            else:
                operations = vals
    print(find_grand_total(lines, operations))

if __name__ == '__main__':
    main()