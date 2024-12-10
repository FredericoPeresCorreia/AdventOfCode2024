column1 = []
column2 = []

with open('PuzzleDay1Pt1.txt', 'r') as file:
    for line in file:
        data = line.strip().split()
        
        column1.append(data[0])
        column2.append(data[1])

column1.sort()
column2.sort()

sum = 0
for x, y in zip(column1, column2):
   #part 1
   # sum += abs(int(x) - int(y))
    sum += int(x) * column2.count(x)

print(sum)