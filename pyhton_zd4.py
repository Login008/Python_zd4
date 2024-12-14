import random

#задание1
rand = random.randint(1,10)
popit = 0

print("Guess the number")
while True:
  n = int(input("number "))
  if (rand == n):
    print("You win with ", popit, "try")
    break
  else:
    print("You don't quess")
    popit += 1;
    
#задание2
mass = input("Letter: ").lower().split(' ')
result = []
temp = []

for i in range(len(mass)):
    if len(temp) == 0 or mass[i] == temp[0]:
        temp.append(mass[i])  
    else:
        result.append(temp)  
        temp = [mass[i]]

if len(temp) > 0:
    result.append(temp)  

final = []  
seen = []  

for item in mass:
    if item not in seen:  
        seen.append(item)  
        gruppa = []
        for i in mass:
            if i == item:
                gruppa.append(i)
        final.append(gruppa)

print(final)

#задание3
mast = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 2, 'Q': 3, 'K': 4, 'A': 11}
random.shuffle(mast)
ochki = 0

while True:
    answer = input("у - take card\nn - finish game\n")
    
    if answer == 'n':
        print("You have", ochki, "ochkov")
        break
    elif answer == 'y':
        card = mast.pop()
        ochki += values[card]  
        
        print("Your card:", card)
        print("Your ochki:", ochki)
        
        if ochki > 21:
            print("You lose! You have more than 21 ochkkov")
            break
        elif ochki == 21:
            print("You winner!")
            break
    else:
        print("y or n")