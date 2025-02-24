import random

roll_list = []
simulations = 10000 
target_value = 25

for i in range(simulations):
    cur_val = 0
    rolls = 0
    while cur_val < target_value:
        roll = random.randint(1,6)
        cur_val += roll
        rolls += 1
        if cur_val == 5:
            cur_val = 15
    roll_list.append(rolls)

print(sum(roll_list)/len(roll_list))