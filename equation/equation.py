import random

class state:
    def __init__(self, arr):
        self.val = arr
    
    def evaluate(self):
        numbers = self.val
        return abs(numbers[0] + 2 * numbers[1] + 3 * numbers[2] + 4 * numbers[3] - 40)

    def __lt__(self, other):
        return self.evaluate() < other.evaluate()

    def __gt__(self, other):
        return self.evaluate() > other.evaluate()





def initialize():
    arr = []
    for i in range(4):
        arr.append(random.randint(0,40))

    return state(arr)

def goal(input_state):
    return input_state.evaluate() == 0

def calculate_total_gen():
    return 4

def fill_crossoverd_parents(crossoverd_parents, parents, index):
    rand_pos = random.randint(0,2)
    
    arr = []
    for i in range(4):
        if i < rand_pos:
            arr.append(parents[index].val[i])
        else:
            item_index = list(parents.keys()).index(index)
            arr.append(list(parents.values())[item_index-1].val[i])
    crossoverd_parents.append(state(arr))


def mutation(population, rand_total_gen):
    rand_num = random.randint(0,10)
    chromosome_index = rand_total_gen / 4
    mutation_element = rand_total_gen % 4
    population[chromosome_index].val[mutation_element] = rand_num





