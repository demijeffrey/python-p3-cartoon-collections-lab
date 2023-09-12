def roll_call_dwarves(dwarves):
    i = 1
    for name in dwarves:
        print(f'{i}. {name}')
        i += 1

def summon_captain_planet(planeteer_calls):
    return [f'{call.title()}!' for call in planeteer_calls]

def long_planeteer_calls(planeteer_calls):
    for call in planeteer_calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(food_list):
    cheese_types = ['cheddar', 'gouda', 'camembert']
    for food in food_list:
        if food in cheese_types:
            return food
        
    return None