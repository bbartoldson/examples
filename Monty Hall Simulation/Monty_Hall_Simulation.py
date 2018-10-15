import random

success = 0
switch = input("\nEnter your strategy (0 for don't switch, 1 for switch):\n")

N = 10000

for i in range(N):
	car = random.randint(0,2)
	choice = random.randint(0,2)
	door_to_reveal = random.randint(0,2)

	while door_to_reveal == car or choice == door_to_reveal:
		door_to_reveal = random.randint(0,2)

	final_choice = 0	
	if switch == "1":
		while final_choice == choice or final_choice == door_to_reveal:
			final_choice += 1
	else:
		final_choice = choice

	success += final_choice == car

if switch == "1":
	print("\nYou switched doors...\n")
else:
	print("\nYou did not switch doors...\n")
print("\nYour win rate was: ", float(success)/N, "\n")
	

	
