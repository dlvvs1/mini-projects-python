import random as r

print("WELCOME TO UNTIL YOU DIE")

# title health of computer and human
total_health_human = 100
total_health_comp = 100

# dicttonary containing mode of attack
dic = {1 : "attack" , 2 : "super attack" , 3 : "heal"}

while(total_health_human > 0 and total_health_comp > 0):
    # user input
    select = int(input("try to kill with!\n1 . attack\n2 . defend\n3 . super attack\n4 . heal\nwhat is youe choice : "))
    human = dic[select]

    # computer input
    i = r.randint(1 , 3)
    comp = dic[i]


    # attack constraints
    human_attack = r.randint(10 , 17)
    comp_attack = r.randint(10 , 17)

    # super attack constraints
    human_super_attack = r.randint(14 , 20)
    comp_super_attack = r.randint(14 , 20)
    
    # heal constraints
    human_heal = r.randint(5 , 15)
    comp_heal = r.randint(5 , 15)

    if human == "attack":
        print(f"\nyour attack is {human} and the attack power is : {human_attack}\n")
    elif human == "super attack":
        print(f"\nyour attack is {human} and the attack power is : {human_super_attack}\n")
    else:
        print(f"\nyour attack is {human} and the attack power is : {human_heal}\n")

    if comp == "attack":
        print(f"\ncomputer attack is {comp} and the attack power is : {comp_attack}\n")
    elif comp == "super attack":
        print(f"\ncomputer attack is {comp} and the attack power is : {comp_super_attack}\n")
    else:
        print(f"\ncomputer attack is {comp} and the attack power is : {comp_heal}\n")
    
    # update health based on attack type and power
    if human == "attack":
        total_health_comp -= human_attack
    elif human == "super attack":
        total_health_comp -= human_super_attack
    else:
        total_health_human += human_heal

    if comp == "attack":
        total_health_human -= comp_attack
    elif comp == "super attack":
        total_health_human -= comp_super_attack
    else:
        total_health_comp += comp_heal

    print(f"now your health is     :{total_health_human}")
    print(f"now opponent health is :{total_health_comp}")

print("\n")
if total_health_human > 0 and total_health_comp < 0 :
    print("-----------------------------🎖️ YOU WON THE MATCH 🎖️--------------------------------------")
else:
    print("😢 SORRY TO SAY YOU LOST")