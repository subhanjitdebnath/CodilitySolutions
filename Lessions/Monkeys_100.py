#100Doors and 100keys and 100monkeys . All doors are closed and every monkeys has the keys to either open or close
# Monkey 1: He will open the doors which comes in table of 1. Ex: 1 2 3 4 5 6 7 8 9 10 ...
# Monkey 2: He will open/close doors which are in table of 2. Ex: 2 4 6 8 10 12 ...

Doors=[False]
n=1

for i in range(1,101):
    Doors.append(False)

for i in range(1,101):
    n=1
    while(n<=100):
        if(n*i<=100):
            Doors[n*i]=not(Doors[n*i])
        n+=1
for i in range(1,101):
    if(Doors[i]):
        print(f"{str(i)} ")
            

