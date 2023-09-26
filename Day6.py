import random

def generate_pass(length):
	characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHILKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+=-[]{}\|;':,./<>?"
	password = ""
	for i in range(length):
		password += random.choice(characters)
	return password
	
pass_length = int(input("Enter the length for password: "))

password = generate_pass(pass_length)

print(f"Your password is : {password}")
