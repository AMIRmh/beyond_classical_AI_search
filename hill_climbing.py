import queens.queens as problem_q
import sys
import random

def main():
    if len(sys.argv) != 3:
        print("Usage python hill_climbing.py [8_queens] [standard/first/random/restart]")
        sys.exit(0)

    problem = None
    if sys.argv[1] == '8_queens':
        problem = problem_q

    if sys.argv[2] == 'standard':
        hill_climbing_standard(problem)
    elif sys.argv[2] == 'first':
        first_best_choice(problem)
    elif sys.argv[2] == 'random':
        random_choice(problem)
    elif sys.argv[2] == 'restart':
        random_restart(problem)


def random_restart(problem):
    cur = problem.initialize()
    init_state = cur

    seen_nodes = 0
    expanded_nodes = 0
    path = []
    while True:
        neighbors = problem.neighbor(cur)
        seen_nodes += len(neighbors)
        best_choice = cur
        for neighbor in neighbors:
            if best_choice < neighbor:
                best_choice = neighbor

        if best_choice == cur:
            cur = problem.random_initialize()
            path = []
            init_state = cur
        elif problem.goal(best_choice):
            path.append(problem.diff(cur, best_choice))
            print_result(problem, seen_nodes, expanded_nodes, best_choice, path, init_state)
        else:
            path.append(problem.diff(cur, best_choice))
            expanded_nodes += 1
            cur = best_choice
            
    print("no answer!!!")

def random_choice(problem):
    cur = problem.initialize()
    init_state = cur
    seen_nodes = 0
    expanded_nodes = 0
    path = []
    while True:
        neighbors = problem.neighbor(cur)
        seen_nodes += len(neighbors)
        best_choices = []
        for neighbor in neighbors:
            if cur < neighbor:
                best_choices.append(neighbor)
        
        best_choice = None
        if len(best_choices) != 0:
            best_choice = random.choice(best_choices)

        if len(best_choices) == 0:
            print_result(problem, seen_nodes, expanded_nodes, cur, path, init_state)
        elif problem.goal(best_choice):
            path.append(problem.diff(cur, best_choice))
            print_result(problem, seen_nodes, expanded_nodes, best_choice, path, init_state)
        else:
            path.append(problem.diff(cur, best_choice))
            expanded_nodes += 1
            cur = best_choice
            
    print("no answer!!!")
    

def first_best_choice(problem):
    cur = problem.initialize()
    init_state = cur
    seen_nodes = 0
    expanded_nodes = 0
    path = []
    while True:
        neighbors = problem.neighbor(cur)
        seen_nodes += len(neighbors)
        best_choice = cur
        for neighbor in neighbors:
            if best_choice < neighbor:
                best_choice = neighbor
                break

        if best_choice == cur:
            print_result(problem, seen_nodes, expanded_nodes, cur, path, init_state)
        elif problem.goal(best_choice):
            path.append(problem.diff(cur, best_choice))
            print_result(problem, seen_nodes, expanded_nodes, best_choice, path, init_state)
        else:
            path.append(problem.diff(cur, best_choice))
            expanded_nodes += 1
            cur = best_choice
            
    print("no answer!!!")
    

def hill_climbing_standard(problem):
    

    cur = problem.initialize()
    init_state = cur
    seen_nodes = 0
    expanded_nodes = 0
    path = []
    while True:
        neighbors = problem.neighbor(cur)
        seen_nodes += len(neighbors)
        best_choice = cur
        for neighbor in neighbors:
            if best_choice < neighbor:
                best_choice = neighbor

        if best_choice == cur:
            print_result(problem, seen_nodes, expanded_nodes, cur, path, init_state)
        elif problem.goal(best_choice):
            path.append(problem.diff(cur, best_choice))
            print_result(problem, seen_nodes, expanded_nodes, best_choice, path, init_state)
        else:
            path.append(problem.diff(cur, best_choice))
            expanded_nodes += 1
            cur = best_choice
            
    print("no answer!!!")


def print_result(problem, seen_nodes, expanded_nodes, cur, path, init_state):
   
    print('init state: ')
    problem.print_init_state(init_state)
    print('seen nodes: ' + str(seen_nodes))
    print('expanded nodes: ' + str(expanded_nodes))
    print('path: ' + str(path))
    print('value: ' + str(cur.evaluate()))
    sys.exit(0)



main()
