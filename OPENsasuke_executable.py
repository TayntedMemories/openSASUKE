def pass_fail_Calculation(): # This is the core/heart of the simulation, so to speak.
    
    def setup():
        ob = input("ENTER OBSTACLE FILE:")
        with open(ob, 'r') as obstacle:
            obstacle_data = yaml.full_load(obstacle)
            print(obstacle_data)
            global obstat
            obstat = next(iter(obstacle_data.values()))
            print(obstat)
        comp = input("ENTER COMPETITOR FILE:")
        with open(comp, 'r') as competitor:
            competitor_data = yaml.full_load(competitor)
            print(competitor_data)
            global compstat
            compstat = next(iter(competitor_data.values()))
    
    def adversary_set():
        chaos_Var = random.uniform(1.5, 1.7)
        global pass_Probability
        pass_Probability = round(((compstat / chaos_Var) / obstat), 2)
        print(f"CHAOS HAS BEEN SET TO {chaos_Var}")
        print(f"WILL THEY PASS; {pass_Probability}")
    
    def execute_Run():
        against_Competitor = round(random.uniform(0.1, 1.3), 2)
        print(f"WILL THEY FAIL; {against_Competitor}")
        print(f"{against_Competitor} > {pass_Probability}")
        if against_Competitor > pass_Probability:
            print("COMPETITOR HAS FAILED.")
        else:
            print("COMPETITOR HAS PASSED")
    
    setup()
    adversary_set()
    execute_Run()

def yaml_Testing():
    file = input()
    with open(file, 'r') as parse:
        data = yaml.full_load(parse)
        print(data)

# UI code goes here.
import yaml
import random

print("Welcome to OPENsasuke. // VERSION: EARLYDEVELOPMENT // By Cain // Copyright is for wusses")
print("""Type in '1' to test the pass/fail function. Type in '2' to test YAML loading. | Type in 'Is This A Ninja Machine?' for a funny.""")
print("What do you want to do?")
selection = input()
if selection == "1":
    print("ENTERING PASS/FAIL DEBUG")
    pass_fail_Calculation()
elif selection == "Is This A Ninja Machine?":
    print("*A* ninja machine, but not THE Ninja Machine.")
elif selection == "2":
    yaml_Testing()
else:
    print("INVALID, BAILING OUT!")
