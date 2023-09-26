# Unit Converter

def cm(centi):
	return centi / 100.0
def mtr(meter):
	return meter /100.0
def mm(mili):
	return mili / 10.0

def main():
	print("unit converter")
	print("1. centimeter to meter")
	print("2. meter to kilometer")
	print("3. milimeter to centimeter")
	print("4. quit")
	
	Opt = int(input("Choose any options >>> "))
	if Opt == 1:
		centi = float(input("enter the length>>> "))
		meter = cm(centi)
		print(f"\n{centi} centimeter is {meter} meter\n\n")
		
	elif Opt == 2:
		meter = float(input("enter the length>>> "))
		km = mtr(meter)
		print(f"\n{meter} meter is {km} kilometer\n\n")
		
	elif Opt == 3:
		mili = float(input("enter the length>>> "))
		centi = mm(mili)
		print(f"\n{mili} milimeter is {centi} centimeter\n\n")
		
	else:
		print("invalid Value")
		
			
while True:
	try:
		main()
		
	except ValueError:
		print("Invalid Value")