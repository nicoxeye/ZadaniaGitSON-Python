def is_critically_balanced():
	temp = float(input("TEMPERATURE IN KELVIN: "))
	ne = float(input("NEUTRONS PER SECOND: "))
	if (temp < 800 or ne > 500 or temp * ne < 500000):
		return True
	else: 
		return False

#UZYCIE   
print(is_critically_balanced())
