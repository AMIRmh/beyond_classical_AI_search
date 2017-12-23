import copy
import math
class state:
    def __init__(self, graph, graph_1, graph_2):
        self.grand_graph = graph
        self.graph_1 = graph_1
        self.graph_2 = graph_2
        self.current_graph, self.disjoinments = self.calculate_graph()

    def calculate_graph(self):
        current_graph = copy.deepcopy(self.grand_graph)
        disjoinments = 0
        for node_1 in self.graph_1:
            for node_2 in self.graph_2:
                if current_graph[node_1][node_2] == 1:
                    current_graph[node_1][node_2] = -1
                    disjoinments += 1
        
        for node_1 in self.graph_2:
            for node_2 in self.graph_1:
                if current_graph[node_1][node_2] == 1:
                    current_graph[node_1][node_2] = -1
        
        return current_graph, disjoinments
         
        

    def evaluate(self):
        return self.disjoinments + abs(len(self.graph_2) - len(self.graph_1))

    def __lt__(self, other):
        return self.evaluate() > other.evaluate()






def initialize():
    arr = []    
    with open("graph/input_graph", "r") as f:
        for line in f:
            line = line.replace('\n', '')
            arr.append(line.split())

    arr = [[int(y) for y in x] for x in arr]

    graph_1 = []
    for i in range(len(arr[0])):
        graph_1.append(i)
    graph_2 = [graph_1.pop(0)]

    init_state = state(arr, graph_1, graph_2)
    return init_state



def neighbor(input_state):
    neighbors = []
    grand_graph = input_state.grand_graph
    graph_1 = input_state.graph_1
    graph_2 = input_state.graph_2
    
    i = 0
    while i < len(graph_1) and len(graph_1) > 1:
        cp_graph_1 = copy.deepcopy(graph_1)
        cp_graph_2 = copy.deepcopy(graph_2)

        node = cp_graph_1.pop(i)
        cp_graph_2.append(node)
        new_state = state(grand_graph, cp_graph_1, cp_graph_2)
        if is_valid_state(new_state):
            neighbors.append(new_state)
        i += 1

    i = 0
    while i < len(graph_2) and len(graph_2) > 1:
        cp_graph_1 = copy.deepcopy(graph_1)
        cp_graph_2 = copy.deepcopy(graph_2)

        node = cp_graph_2.pop(i)
        cp_graph_1.append(node)
        new_state = state(grand_graph, cp_graph_1, cp_graph_2)
        if is_valid_state(new_state):
            neighbors.append(new_state)
        i += 1
        

    return neighbors

def is_valid_state(new_state):
    seen = [False for i in range(len(new_state.graph_1))]
    seen[0] = True
    fill_valid_path(new_state, new_state.graph_1, new_state.graph_1[0], seen)
    for true in seen:
        if not true:
            return False
    
    seen = [False for i in range(len(new_state.graph_2))]
    seen[0] = True
    fill_valid_path(new_state, new_state.graph_2, new_state.graph_2[0], seen)
    for true in seen:
        if not true:
            return False

    return True

def fill_valid_path(new_state, graph, node, seen):
    for graph_node in graph:
        if not seen[graph.index(graph_node)]:
            if new_state.current_graph[node][graph_node] == 1:
                seen[graph.index(graph_node)] = True
                fill_valid_path(new_state, graph, graph_node, seen)



def diff(cur, choosed_node):
    if len(cur.graph_1) > len(choosed_node.graph_1) :
        cp_choosed_graph_1 = copy.deepcopy(choosed_node.graph_1)
        cp_cur_graph_1 = copy.deepcopy(cur.graph_1)
        for node in cp_choosed_graph_1:
            cp_cur_graph_1.remove(node)

        return str(cp_cur_graph_1.pop(0)) + ' graph_1 -> graph_2'
    else:
        cp_choosed_graph_2 = copy.deepcopy(choosed_node.graph_2)
        cp_cur_graph_2 = copy.deepcopy(cur.graph_2)
        for node in cp_choosed_graph_2:
            cp_cur_graph_2.remove(node)

        return str(cp_cur_graph_2.pop(0)) + ' graph_2 -> graph_1'





def print_state(init_state):
    print("current graph: ")
    for i in init_state.current_graph:
        print(i)
    print("graph1: " + str(init_state.graph_1))
    print("graph2: " + str(init_state.graph_2))
    print("\n")
    


def goal(input_state):
    return False
