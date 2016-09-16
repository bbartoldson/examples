import random

success = 0
switch = input("\nEnter your strategy (0=don't switch, 1=switch):\n")
N = 10000

for i in range(N):
	car = random.randint(0,2)
	choice = random.randint(0,2)
	door_to_reveal = random.randint(0,2)

	while door_to_reveal == car or choice == door_to_reveal:
		door_to_reveal = random.randint(0,2)

	final_choice = choice
	
	if switch:
		while choice == final_choice or final_choice == door_to_reveal:
			final_choice = random.randint(0,2)

	success += final_choice == car

if switch:
	print "\nYou switched doors...\n"
else:
	print "\nYou did not switch doors...\n"
print "\nYour win rate was: ", float(success)/N, "\n"
	

	
