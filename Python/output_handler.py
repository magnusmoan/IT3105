def show_solutions(step_by_step, solutions, time_used):
    print "Found " + str(len(solutions)) + " solutions"
    print "Time used: " + str(time_used)
    show_step_by_step = raw_input("\nDo you want to see step by step for the first solution? (YES/NO): ").lower()
    
    if show_step_by_step == "yes":
        for solution in step_by_step:
            print solution
    
    show_all_solutions = raw_input("\nDo you want to see all solutions? (YES/NO): ").lower()
    
    if show_all_solutions == "yes":
        for solution in solutions:
            print solution
