safe = 0;

def is_safe(numbers): 
    increasing = all(numbers[i] <= numbers[i+1] and 1 <= numbers[i+1] - numbers[i] <= 3 for i in range(len(numbers)-1)) 
    decreasing = all(numbers[i] >= numbers[i+1] and 1 <= numbers[i] - numbers[i+1] <= 3 for i in range(len(numbers)-1)) 
    return increasing or decreasing


def remove_one_element(numbers):
    for i in range(len(numbers)):
        modified = numbers[:i] + numbers[i+1:]  
        if is_safe(modified):
            return True
    return False

with open('./inputs/Day2.txt', 'r') as file: 
    for line in file: 
        numbers = list(map(int, line.strip().split())) 
        if is_safe(numbers) or remove_one_element(numbers): 
            safe += 1 

print(safe)