import graph.graph as problem_g
import sys
import random
import math

def main():

    if len(sys.argv) != 3:
        print("Usage python simulated_annealing.py [graph] [1/2/3]")
        sys.exit(0)


    problem = None 
    if sys.argv[1] == 'graph':
        problem = problem_g

    
    if sys.argv[2] == '1':
        simulated_annealing_linear_step_reduce(problem)
    elif sys.argv[2] == '2':
        simulated_annealing_exponential_step_reduce(problem)
    elif sys.argv[2] == '3':
        simulated_annealing_square_root_step_reduce(problem)

def simulated_annealing_square_root_step_reduce(problem):

    cur = problem.initialize()
    init_state = cur
    seen_nodes = 0
    expanded_nodes = 0
    path = []
    chance_to_choose_worse = 10000
    
    while True:
        neighbors = problem.neighbor(cur)
        seen_nodes += len(neighbors)
        choosed_node = random.choice(neighbors)
        while choosed_node < cur and chance_to_choose_worse < random.randint(0,10000):
            choosed_node = random.choice(neighbors)

        chance_to_choose_worse = int(math.sqrt(chance_to_choose_worse))

        if problem.goal(choosed_node):
            path.append(problem.diff(cur, choosed_node))
            print_result(problem, seen_nodes, expanded_nodes, choosed_node, path, init_state)
        elif chance_to_choose_worse == 1:
            path.append(problem.diff(cur, choosed_node))
            print_result(problem, seen_nodes, expanded_nodes, choosed_node, path, init_state)
        else:
            path.append(problem.diff(cur, choosed_node))
            expanded_nodes += 1
            cur = choosed_node
            
    print("no answer!!!")

def simulated_annealing_exponential_step_reduce(problem):

    cur = problem.initialize()
    init_state = cur
    seen_nodes = 0
    expanded_nodes = 0
    path = []
    chance_to_choose_worse = 100
    
    while True:
        neighbors = problem.neighbor(cur)
        seen_nodes += len(neighbors)
        choosed_node = random.choice(neighbors)
        while choosed_node < cur and chance_to_choose_worse < random.randint(0,100):
            choosed_node = random.choice(neighbors)

        chance_to_choose_worse /= 2

        if problem.goal(choosed_node):
            path.append(problem.diff(cur, choosed_node))
            print_result(problem, seen_nodes, expanded_nodes, choosed_node, path, init_state)
        elif chance_to_choose_worse == 0:
            path.append(problem.diff(cur, choosed_node))
            print_result(problem, seen_nodes, expanded_nodes, choosed_node, path, init_state)
        else:
            path.append(problem.diff(cur, choosed_node))
            expanded_nodes += 1
            cur = choosed_node
            
    print("no answer!!!")
    

def simulated_annealing_linear_step_reduce(problem):

    cur = problem.initialize()
    init_state = cur
    seen_nodes = 0
    expanded_nodes = 0
    path = []
    chance_to_choose_worse = 100
    
    while True:
        neighbors = problem.neighbor(cur)
        seen_nodes += len(neighbors)
        choosed_node = random.choice(neighbors)
        while choosed_node < cur and chance_to_choose_worse < random.randint(0,100):
            choosed_node = random.choice(neighbors)

        chance_to_choose_worse -= 5

        if problem.goal(choosed_node):
            path.append(problem.diff(cur, choosed_node))
            print_result(problem, seen_nodes, expanded_nodes, choosed_node, path, init_state)
        elif chance_to_choose_worse == 0:
            path.append(problem.diff(cur, choosed_node))
            print_result(problem, seen_nodes, expanded_nodes, choosed_node, path, init_state)
        else:
            path.append(problem.diff(cur, choosed_node))
            expanded_nodes += 1
            cur = choosed_node
            
    print("no answer!!!")


def print_result(problem, seen_nodes, expanded_nodes, cur, path, init_state):
   
    print('init state: ')
    problem.print_state(init_state)
    print('seen nodes: ' + str(seen_nodes))
    print('expanded nodes: ' + str(expanded_nodes))
    print('\nresult state: ')
    problem.print_state(cur)
    print('path: ')
    for p in path:
        print(p)
    print('value: ' + str(cur.evaluate()))
    sys.exit(0)






main()
