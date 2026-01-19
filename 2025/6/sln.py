

def find_grand_total(nums: list[list[int]], ops: list[str]) -> int:
    total = 0
    for i in range(len(ops)):
        if ops[i] == '+':
            total += nums[0][i] + nums[1][i] + nums[2][i] + nums[3][i]
        else:
            total = total + (nums[0][i] * nums[1][i] * nums[2][i] * nums[3][i])
    return total

def add_0s_to_num(num: str, to_add: int) -> str:
    if to_add == 0:
        return num
    else:
        num =  num + ("0" * to_add)
    return num

def make_nums_same_length(num1: str, num2: str, num3: str, num4) -> tuple[str, str, str, str]:
    max_length = max(len(num1), max(len(num2), len(num3)))
    num1 = add_0s_to_num(num1, len(num1) - max_length)
    num2 = add_0s_to_num(num2, len(num2) - max_length)
    num3 = add_0s_to_num(num3, len(num3) - max_length)
    num4 = add_0s_to_num(num4, len(num4) - max_length)
    values = []
    for j in range(len(num1) - 1, -1, -1):
        value = (num1[j] * 1000) + (num2[j] * 100) + (num3[j] * 10)
    return num1, num2, num3, num4

def find_grand_total_pt2(nums: list[list[int]], ops: list[str]) -> int:
    total = 0
    for i in range(len(ops)):
        num1 = str(nums[i][0])
        num2 = str(nums[i][1])
        num3 = str(nums[i][2])
        num4 = str(nums[i][3])
        num1, num2, num3 = make_nums_same_length(num1, num2, num3, num4)

        for j in range(len(num1) - 1, -1, -1):
            v
            if ops[i] == '+':
                total += num1[j] + num2[j] + num3[j] + num4[j]


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
    #print(find_grand_total(lines, operations))
    print(find_grand_total_pt2(lines, operations))

if __name__ == '__main__':
    main()