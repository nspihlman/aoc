
class LockTracker:
    def __init__(self):
        self.cur_pos = 50
        self.zero_ct = 0

    def move_dial(self, move: str) -> None:
        print(f"{move}")
        start_zero = self.cur_pos == 0
        net_move = int(move[1:]) % 100
        pass_zero = int(move[1:]) // 100
        self.zero_ct += pass_zero
        if move[0] == "L":
            self.cur_pos -= net_move
        else:
            self.cur_pos += net_move
        self._validate_dial(start_zero)


    def _validate_dial(self, start_zero: bool):
        if self.cur_pos == 0:
            self.zero_ct += 1
        elif self.cur_pos < 0:
            self.cur_pos = 100 + self.cur_pos
            if not start_zero:
                self.zero_ct += 1
        elif self.cur_pos > 99:
            self.cur_pos = self.cur_pos % 100
            self.zero_ct += 1


    def get_zero(self):
        return self.zero_ct


def main():
    my_lock = LockTracker()

    with open("in.txt") as f:
        for line in f:
            my_lock.move_dial(line.rstrip())
    print(my_lock.get_zero())


if __name__ == "__main__":
    main()