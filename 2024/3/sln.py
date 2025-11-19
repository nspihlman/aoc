def is_do(idx, line: str) -> bool:
    do_check: str = line[idx:idx+4]
    if do_check == 'do()':
        return True
    return False

def is_dont(idx, line: str) -> bool:
    dont_check:str = line[idx:idx+7]
    if dont_check == "don't()":
        return True
    return False
# got it wrong, answer is too high
def valid_mul(idx: int, line: str, do: bool):
    total_sum = 0
    while(idx < len(line)):
        if line[idx] == 'm' and do:
            mul_start: str = line[idx:idx+4]
            if mul_start != 'mul(':
                idx += 1
                continue
            idx += 4
            dig_found = 0
            first_num: str = ""
            while(line[idx].isdigit()):
                dig_found += 1
                first_num += line[idx]
                idx += 1
            if dig_found < 1 or dig_found > 3 or line[idx] != ',':
                continue
            idx += 1
            dig_found = 0
            second_num: str = ""
            while(line[idx].isdigit()):
                dig_found += 1
                second_num += line[idx]
                idx+=1
            if dig_found < 1 or dig_found > 3 or line[idx] != ')':
                continue
            idx += 1
            total_sum += int(first_num) * int(second_num)
        elif line[idx] == 'd':
            if is_do(idx, line):
                do = True
                idx += 4
            elif is_dont(idx, line):
                do = False
                idx += 7
            else:
                idx += 1
        else:
            idx += 1
    return total_sum, do


def main():
    total_sum = 0
    do = True
    with open('in.txt') as f:
        for line in f:
            result, do = valid_mul(0, line, do)
            total_sum += result
    print(total_sum)

if __name__ == '__main__':
    main()