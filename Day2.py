print("Percent Calculator")

Maths = int(input("Enter your Maths marks: "))
Science = int(input("Enter your Science marks: "))
Sscience = int(input("Enter your Social science marks: "))
English = int(input("Enter your English Marks: "))
Hindi = int(input("Enter Your Hindi marks: "))

Gtotal = Maths + Science + Sscience + English + Hindi

Percent = Gtotal/5


if Percent >= 60:
	print(f"Congratulations! you are first with {Percent}%")
elif Percent >= 45:
	print(f"Congratulations! you are Second with {Percent}%")
elif Percent >= 33:
	print(f"Congratulations! you passed with {Percent}%")
else:
	print(f"Sorry you failed with {Percent}%")