def reactor_efficiency(voltage, current, theoretical_max_power):
	generated_power = voltage * current
	percentage =  (generated_power / theoretical_max_power) * 100
	
	print(f"GENERATED POWER: {generated_power}, THEORETICAL MAX POWER: {theoretical_max_power}, EFFICIENCY: {percentage}%")

	if percentage >= 80:
		print('green')
	elif percentage >= 60:
		print('orange')
	elif percentage >= 30:
		print('red')
	else:
		print('black')
	
vol = float(input('VOLTAGE: '))
cur = float(input('CURRENT: '))
theor_max = float(input('WHATS THE THEORETICAL MAX POWER: '))

reactor_efficiency(vol, cur, theor_max)
