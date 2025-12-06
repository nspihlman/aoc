

# can start from the back, then always look for the next largest one. because we know that the value has to be at least
# x from the end
def find_max_voltage(volts: str):
    mx = 0
    sec_max = 0
    for i in range(len(volts) - 1):
        if int(volts[i]) > mx:
            mx = int(volts[i])
            sec_max = 0
            if i == len(volts) - 2:
                return (mx*10) + int(volts[-1])
        elif int(volts[i]) > sec_max:
            sec_max = int(volts[i])
    if int(volts[-1]) > sec_max:
        sec_max = int(volts[-1])
    return (mx*10) + sec_max

def find_max_voltage_12val(volts: str):
    mx = 0
    voltage = ""
    # farthest you can go back is -len, but that is a valid index (while len is not a valid index)
    mx_idx = -1
    start_idx = -12
    idx = start_idx
    end = ((-1) * len(volts)) - 1
    while len(voltage) < 12:
        while idx > end:
            if int(volts[idx]) >= mx:
                mx = int(volts[idx])
                mx_idx = idx
            idx -= 1
        voltage = voltage + str(mx)
        end = mx_idx
        start_idx += 1
        idx = start_idx
        mx = 0
    print(voltage)
    return int(voltage)


def main():
    total = 0
    with open('in.txt') as f:
        for line in f:
            total += find_max_voltage_12val(line.rstrip())
    print(total)

if __name__ == '__main__':
    main()