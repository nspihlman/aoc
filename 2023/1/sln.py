

class CalibrationValue:
    def __init__(self):
        self._total = 0

    def add_value(self, value):
        self._total += value

    def get_value(self):
        return self._total

def parse_value_from_line(line: str) -> int:
    left = 0
    right = len(line) - 1
    while not line[left].isdigit():
        left += 1
    while not line[right].isdigit():
        right -= 1
    int_str = line[left] + line[right]
    return int(int_str)


def main():
    cal_val = CalibrationValue()
    with open('in.txt') as f:
        for line in f:
            cal_val.add_value(parse_value_from_line(line))
    print(cal_val.get_value())


if __name__ == '__main__':
    main()