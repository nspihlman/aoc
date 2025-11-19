# push into a 2d vector. for each x found, call helper functions to check forward, backwards, up, down,
# upleft, upright, downleft, downright
def check_backwards(search: list[list[str]], row: int, col: int) -> bool:
    if col > 0 and search[row][col-1] == 'M':
        if col > 1 and search[row][col-2] == 'A':
            if col > 2 and search[row][col-3] == 'S':
                return True
    return False

def check_forwards(search: list[list[str]], row: int, col: int) -> bool:
    if col < (len(search[row]) - 3):
        if search[row][col+1] == 'M':
            if search[row][col+2] == 'A':
                if search[row][col+3] == 'S':
                    return True
    return False

def check_up(search: list[list[str]], row: int, col: int) -> bool:
    if row >= 3:
        if search[row-1][col] == 'M':
            if search[row-2][col] == 'A':
                if search[row-3][col] == 'S':
                    return True
    return False

def check_down(search: list[list[str]], row: int, col: int) -> bool:
    if row < (len(search) - 3):
        if search[row+1][col] == 'M':
            if search[row+2][col] == 'A':
                if search[row+3][col] == 'S':
                    return True
    return False

def check_upleft(search: list[list[str]], row: int, col: int) -> bool:
    if row >= 3 and col >= 3:
        if search[row-1][col-1] == 'M':
            if search[row-2][col-2] == 'A':
                if search[row-3][col-3] == 'S':
                    return True
    return False

def check_upright(search: list[list[str]], row: int, col: int) -> bool:
    if row >= 3 and col < (len(search[row]) - 3):
        if search[row-1][col+1] == 'M':
            if search[row-2][col+2] == 'A':
                if search[row-3][col+3] == 'S':
                    return True
    return False

def check_downleft(search: list[list[str]], row: int, col: int) -> bool:
    if row < (len(search) - 3) and col >= 3:
        if search[row+1][col-1] == 'M':
            if search[row+2][col-2] == 'A':
                if search[row+3][col-3] == 'S':
                    return True
    return False

def check_downright(search: list[list[str]], row: int, col: int) -> bool:
    if row < (len(search) - 3) and col < (len(search[row]) - 3):
        if search[row+1][col+1] == 'M':
            if search[row+2][col+2] == 'A':
                if search[row+3][col+3] == 'S':
                    return True
    return False

def checkall(search: list[list[str]], row: int, col: int) -> int:
    total = 0
    if check_backwards(search, row, col):
        total+=1
    if check_forwards(search, row, col):
        total+=1
    if check_up(search, row, col):
        total+= 1
    if check_down(search, row, col):
        total+=1
    if check_downleft(search, row, col):
        total+= 1
    if check_downright(search, row, col):
        total+=1
    if check_upleft(search, row, col):
        total+=1
    if check_upright(search, row, col):
        total+=1
    return total

def check_mas_topleft(search, row, col)->bool:
    # other M can be in two different places: bottom left or top right. first check the MAS exists
    if row < len(search) - 2 and col < len(search[row]) - 2:
        if search[row+1][col+1] == 'A' and search[row+2][col+2] == 'S':
            if (search[row][col+2] == 'M' and search[row+2][col] == 'S') or (
                search[row+2][col] == 'M' and search[row][col+2] == 'S'
            ):
                return True
    return False

def check_mas_topright(search, row, col)->bool:
    # other M has to be bottom right
    if row < len(search) - 2 and col >= 2:
        if search[row+1][col-1] == 'A' and search[row+2][col-2] == 'S':
            if search[row+2][col] == 'M' and search[row][col-2] == 'S':
                return True
    return False

def check_mas_botleft(search, row, col)->bool:
    if row >= 2 and col < len(search[row]) - 2:
        if search[row-1][col+1] == 'A' and search[row-2][col+2] == 'S':
            if search[row][col+2] == 'M' and search[row-2][col] == 'S':
                return True
    return False

def checkx_mas(search, row, col):
    # move top down so only check down directions: i'm either starting top left or top right. 
    # if i'm top left, then the other one is bottom left or top right. 
    # if i'm top right, other is bottom right (because top left has been checked by ordering)
    # then check for up and to left and up and to right (and i'm bottom left) - can't be bottom right from ordering
    total = 0
    if check_mas_botleft(search, row, col):
        total += 1
    if check_mas_topleft(search, row, col):
        total += 1
    if check_mas_topright(search, row, col):
        total += 1
    return total

def main():
    wordsearch = []
    total = 0
    with open("in.txt") as f:
        for line in f:
            letters = []
            for letter in line:
                letters.append(letter)
            wordsearch.append(letters)
    for row in range(len(wordsearch)):
        for col in range(len(wordsearch[row])):
            if wordsearch[row][col] == 'M':
                total += checkx_mas(wordsearch, row, col)
    print(total)
            
    

if __name__ == "__main__":
    main()