from utils import fitness

def show_solutions(step_by_step, solutions, time_used, n, backtracking):
    print "Found " + str(len(solutions)) + " solutions"
    print "Time used: " + str(time_used)
    show_step_by_step = raw_input("\nDo you want to see step by step for the first solution? (YES/NO): ").lower()
    
    if show_step_by_step == "yes" or show_step_by_step == "y":
        if backtracking:
            print_step_by_step_backtracking(step_by_step, n)
        else:
            print_step_by_step_heuristic(step_by_step, n)
    
    show_all_solutions = raw_input("\nDo you want to see all solutions? (YES/NO): ").lower()
    
    if show_all_solutions == "yes" or show_step_by_step == "y":
        for solution in solutions:
            print format_solution(solution)


def print_step_by_step_backtracking(step_by_step, n):
    for step in step_by_step:
        step = map(lambda x: x + 1, step)
        if len(step) != n:
            for _ in range(len(step), n):
                step.append("-")
        print format_solution_backtracking(step)

def print_step_by_step_heuristic(step_by_step, n):
    max_fitness = (n*(n-1))/2
    print "\n FITNESS (% of max) | STEP BY STEP"
    print "--------------------" + '-'*(10 + 2*n)
    for step in step_by_step:
        fitness_percent = 100*(float(fitness(step, max_fitness))/max_fitness)
        percent_string = "%.2f" % fitness_percent
        percent_string += "%"
        print percent_string.center(20, " ") + "|" + "  " + format_solution(step)

def format_solution(solution):
    return " ".join(map(str, map(lambda x: x + 1, solution)))

def format_solution_backtracking(solution):
    return " ".join(map(str, solution))
