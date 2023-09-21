import random

print("Welcome to guess the number game...")
print("Created by Anjaan for fun...")

# creating a random value
secNum = random.randint(1, 20)

trying = 0

while True:
	try:
		guess = int(input("Guess any number between 1 to 20: "))
		
		trying += 1
		
		if guess == secNum:
			print(f"Congratulation! you guess the right number in {trying} attempts")
			break
			
		elif guess > secNum:
			print("Oops! you guess higher number...")
			
		else:
			print("Oops! you guess lower number...")
			
	except ValueError:
		print("Please Enter a valid value...")