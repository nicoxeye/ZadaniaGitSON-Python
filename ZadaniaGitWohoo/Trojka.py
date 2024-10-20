def fail_safe(temperature, neutrons_per_second, threshold):
    low_threshold = 0.9 * threshold
    upper_threshold = 1.1 * threshold

    if temperature * neutrons_per_second < low_threshold:
        return 'LOW'
    if low_threshold <= temperature * neutrons_per_second <= upper_threshold:
        return 'NORMAL'
    else: #wyzej niz 1.1 progu
        return 'HIGH'

#UZYCIE   
temp = float(input('TEMPERATURE IN KELVINS: '))
neutrons = float(input('NEUTRONS PER SECOND: '))
thre = float(input('THRESHOLD: '))

print(fail_safe(temp, neutrons, thre))
