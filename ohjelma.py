tie_round = 0
won_round = 0
played_round = 0

while True:	
    user_chose = input("Foot, Nuke or Cockroach? (Quit ends):")
    if user_chose == "Foot" or user_chose == "Nuke" or user_chose == "Cockroach":
        print("You chose:", user_chose)
    elif user_chose == "Quit":
        break
    else:
        print("Incorrect selection.")
        continue
		
    #let's pick a random number between 0 and 2
    #1 (Foot), 2(Nuke), 3(Cockroach)
    import random
    cpu_chose = random.randint(1,4)
    if cpu_chose == 1:
        print("Computer chose: Foot")
    elif cpu_chose == 2:
        print("Computer chose: Nuke")
    else:
        print("Computer chose: Cockroach")
		
    #Let's check the result
	#case1. draw
    if (user_chose =="Foot" and cpu_chose == 1) or (user_chose =="Cockroach" and cpu_chose == 3):
        print("It is a tie!")
        tie_round += 1
    #case2. win
    elif (user_chose =="Foot" and cpu_chose == 3) or (user_chose =="Cockroach" and cpu_chose == 2) or (user_chose =="Nuke" and cpu_chose == 1):
        print("You WIN!")
        won_round += 1
    #case3. both-lose
    elif (user_chose =="Nuke" and cpu_chose == 2):
        print("Both LOSE!")
    #case4. lose
    else:
        print("You LOSE!")
		
    played_round += 1
	
#Last message
print("You played" ,played_round, "rounds, and won" ,won_round, "rounds, playing tie in" ,tie_round, "rounds.")