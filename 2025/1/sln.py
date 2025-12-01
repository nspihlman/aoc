
class LockTracker:
    def __init__(self):
        self.cur_pos = 50
        self.zero_ct = 0

    def move_dial(self, move: str) -> None:
        total_move = int(move[1:]) % 100
        print(f"{total_move} from {move}")
        if move[0] == "L":
            self.cur_pos -= total_move
        else:
            self.cur_pos += total_move
        print(f"{self.cur_pos} curpos after move")
        self._validate_dial()
        print(f"{self.cur_pos} curpos after validation")
        self._check_zero()

    def _validate_dial(self):
        if self.cur_pos < 0:
            self.cur_pos = 100 + self.cur_pos
        elif self.cur_pos > 99:
            self.cur_pos = self.cur_pos % 100

    def _check_zero(self):
        if self.cur_pos == 0:
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