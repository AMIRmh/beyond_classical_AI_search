import copy
import random
class state:
    def __init__(self, ground):
        self.val = ground
        self.queens = self.find_queens()
    
    def __lt__(self, other):
        return self.evaluate() > other.evaluate()

    def evaluate(self):
        ground = self.val
        queens = self.queens
        price = 0
        for col, row in queens.items():
            for check_col in range(int(col) + 1, 8, 1):
                if ground[row][check_col] == 1:
                    price += 1
            check_row = row - 1
            check_col = int(col) + 1
            while check_row > 0 and check_col < 8:
                if ground[check_row][check_col] == 1:
                    price += 1
                check_col += 1
                check_row -= 1
    
            check_row = row + 1
            check_col = int(col) + 1
            while check_row < 8 and check_col < 8:
                if ground[check_row][check_col] == 1:
                    price += 1
                check_col += 1
                check_row += 1
                    
    
        return price

    def find_queens(self):
        queens = {}
        for col in range(8):
            for row in range(8):
                if self.val[row][col] == 1:
                    queens[str(col)] = row
                    break
        return queens




def initialize():
    arr = [[] for i in range(8)]    
    with open("queens/input_8_queens", "r") as f:
        i = 0
        for line in f:
            line = line.replace(' ', '').replace('\n', '')
            arr[i].extend(line)
            i = i + 1
    
    arr = [[int(y) for y in x] for x in arr]
    init_state = state(arr)
    return init_state

def random_initialize():
    row_num = [i for i in range(8)]
    col_num = [i for i in range(8)]
    arr = [[0 for i in range(8)] for j in range(8)]
    
    i = 0
    while i < 8:
        row = random.choice(row_num)
        col = random.choice(col_num)

        col_num.remove(col)
        arr[row][col] = 1
        i += 1

    init_state = state(arr)
    return init_state


def neighbor(input_state):
    ground = input_state.val

    result = []
    for col, row in input_state.queens.items():
        for row_range in range(8):
            if row_range != row:
                cp = copy.deepcopy(ground)
                cp[row][int(col)] = 0
                cp[row_range][int(col)] = 1    
                result.append(state(cp))

    return result


def goal(input_state):
    if input_state.evaluate() == 0:
        return True
    return False


def diff(cur, best_choice):
    for i in range(8):
        cur_row = cur.queens.get(str(i))
        best_choice_row = best_choice.queens.get(str(i))
        if cur_row != best_choice_row:
            return {str(i): best_choice_row}


def print_init_state(init_state):
    for i in range(8):
        print(init_state.val[i])











