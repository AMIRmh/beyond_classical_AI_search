import equation.equation as problem_e
import copy
import sys
import random


POPULATION = 6
CROSSOVER_RATE = 0.3
MUTATION_RATE = 0.1
ITERATION = 500
TOTAL_GEN = 0

def main():
    if len(sys.argv) != 2:
        print("Usage python genetic.py [equation]")
        sys.exit(0)

    problem = None
    if sys.argv[1] == 'equation':
        problem = problem_e

    global TOTAL_GEN
    TOTAL_GEN = problem.calculate_total_gen()

    genetic(problem)


def genetic(problem):

    #initialize
    init_population = []
    for i in range(POPULATION):
        init_population.append(problem.initialize())

    result_best = []
    result_worst = []
    result_avg = []
    found = False
    for iteration in range(ITERATION):
        if found:
            break
        #selection
        f_obj = []
        for member in init_population:
            f_obj.append(member.evaluate())

        sum_fitness = 0
        fitness = []
        for f in f_obj:
            num = float(1)/(1 + f)
            fitness.append(num)
            sum_fitness += num

        probability = []
        for i in range(POPULATION):
            if i == 0:
                probability.append(fitness[i] / sum_fitness)
            else:
                probability.append(probability[i-1] + fitness[i] / sum_fitness)

        population = []
        for i in range(POPULATION):
            rand_num = random.uniform(0,1)
            for j in range(POPULATION):
                if j == 0:
                    if rand_num < probability[j]:
                        population.append(init_population[j])
                #        print(init_population[j].evaluate())
                        break
                else:
                    if rand_num < probability[j] and rand_num > probability[j-1] :
                 #       print(init_population[j].evaluate())
                        population.append(init_population[j])
                        break

        #crossover
        parents = {}
        while len(parents) == 0:
            for i in range(POPULATION):
                if random.uniform(0,1) < CROSSOVER_RATE:
                    parents[i] = population[i]
        
        crossoverd_parents = []
        for i in range(POPULATION):
            if i not in parents:
                crossoverd_parents.append(population[i])
            else:
                problem.fill_crossoverd_parents(crossoverd_parents, parents, i)


        population = crossoverd_parents

        #mutation
        for i in range(int(TOTAL_GEN * POPULATION * MUTATION_RATE)):
            rand_total_gen = random.randint(0, TOTAL_GEN * POPULATION - 1)
            problem.mutation(population, rand_total_gen)
        

        #print time:)
        worst_member  = population[0]
        best_member  = population[0]
        sum_values = 0
        for member in population:
            if worst_member < member:
                worst_member = member
            if best_member > member:
                best_member = member
            sum_values += member.evaluate()
        
        print("\n\n\n")
        print("turn: " + str(iteration))
        print("worst member: " + str(worst_member.evaluate()))
        print("best member: " + str(best_member.evaluate()))
        print("average member: " + str(sum_values / POPULATION))
        result_best.append([iteration, best_member.evaluate()])
        result_worst.append([iteration, worst_member.evaluate()]),
        result_avg.append([iteration, sum_values / POPULATION])



        #goal check
        for member in population:
            if problem.goal(member):
                print("\n\ngoal member found: " + str(member.val))
                found = True
                


    if not found:
        best = population[0]
        for i in range(POPULATION):
            if population[i] < best:
                best = population[i]
        print("best member: " + str(best.val))
        print("best memeber value: " + str(best.evaluate()))
    best_f = open('equation/best.csv', 'w')
    worst_f = open('equation/worst.csv', 'w')
    avg_f = open('equation/avg.csv', 'w')
    for line in range(len(result_avg)):
        best_line = str(result_best[line])
        worst_line = str(result_worst[line])
        avg_line = str(result_avg[line])
        best_f.write(best_line.replace('[','').replace(']',''))
        worst_f.write(worst_line.replace('[','').replace(']',''))
        avg_f.write(avg_line.replace('[','').replace(']',''))
        best_f.write("\n")
        worst_f.write("\n")
        avg_f.write("\n")
    best_f.close()
    worst_f.close()
    avg_f.close()

main()
