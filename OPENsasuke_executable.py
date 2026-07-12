def pass_fail_Calculation(): # This is the core/heart of the simulation, so to speak.
    
    def loaddata():
        
        ob = input("ENTER OBSTACLE FILE:")
        
        with open(ob, 'r') as obstacle:
            global obstacle_data
            
            obstacle_data = yaml.full_load(obstacle)
                    
        comp = input("ENTER COMPETITOR FILE:")
        
        with open(comp, 'r') as competitor:
            
            global competitor_data
            
            competitor_data = yaml.full_load(competitor)

    def get_common_keys():
        
        global obkeys
        
        obkeys = set(obstacle_data.keys()) if isinstance(obstacle_data, dict) else set()
        
        print(obkeys)
        
        global compkeys
        
        compkeys = set(competitor_data.keys()) if isinstance(competitor_data, dict) else set()  
        
        print(compkeys)

        global common
        
        common = obkeys & compkeys
        
        print(f"COMMON:", common, type(common))
        global common_length 
        common_length = len(common)
        
    def setup_individual_relevant_values(): # This won't work for when there are more than 2 common values.
        # I don't give a fuck and I will patch this eventually. Don't make obstacles with more than 2 adversarial keys! 
        val = list()
        
        loopiterator = 0

        for val in common:
            
            x = val
            
            y = val
            
            loopiterator = loopiterator + 1
            
            if loopiterator == 1:
                
                global x1
                
                global y1
                
                x1 = obstacle_data.get(val)
                
                y1 = competitor_data.get(val)
            
            elif loopiterator == 2:
                
                global x2
                
                global y2
                
                x2 = obstacle_data.get(val)
                
                y2 = competitor_data.get(val)
    

    def adversary_set():
        # SETUP VALUES
        global obdiff 
        obdiff = ((x1 + x2) / 2) # hard coded values make my life easier.  this just makes an average of two values
        global compdiff 
        compdiff = ((y1 + y2) / 2) # hard coded values make my life easier. this just makes an average of two values
        # SETUP VALUES
        
        chaos_Var = random.uniform(1.5, 1.7)
       
        global pass_Probability
        
        pass_Probability = round(((compdiff / chaos_Var) / obdiff), 2)
        
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
    
 # FUNCTION EXECUTION   
    loaddata()

    get_common_keys()

    setup_individual_relevant_values()
    
    adversary_set()
    
    execute_Run()
# FUNCTION EXECUTION

# UI code goes here.

import yaml

import random

print("Welcome to OPENsasuke. // VERSION: EARLYDEVELOPMENT2 // By Cain // COPYLEFT!")

print("""Type in '1' to test the pass/fail function. Type in '2' to test YAML loading. | Type in 'Is This A Ninja Machine?' for a funny.""")

print("What do you want to do?")

selection = input()

if selection == "1":
    
    print("ENTERING PASS/FAIL DEBUG")
    
    pass_fail_Calculation()

elif selection == "Is This A Ninja Machine?":
    
    print("*A* ninja machine, but not THE Ninja Machine.")

else:
    
    print("INVALID, BAILING OUT!")
