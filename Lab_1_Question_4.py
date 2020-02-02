numberOfMinutesPassed = int(input("Enter the number of minutes passed"))

hours = numberOfMinutesPassed // 60

minutes = numberOfMinutesPassed % 60

print(str(hours) + " " + str(minutes))