DISTANCE_FROM_UNIVERSITY = 4 #miles
BUS_SPEED = 25 #mph
BUS_STOP = 2 #minutes
NUMBER_OF_STOPS = 10

def timeTakenByBus():
    time = DISTANCE_FROM_UNIVERSITY / BUS_SPEED * 60
    finalTime = time + timeSpentOnStops()
    return finalTime

def timeSpentOnStops():
    return 2 * 10

def timeTakenToRun():
    firstMileTime =  7 * 60
    secondAndThirdMileTime = 2/(15 * 60)
    lastMile = 7 * 60
    return firstMileTime + secondAndThirdMileTime + lastMile

print("Bus will take " + str(timeTakenByBus()) + " minutes")
print("Jogging will take " + str(timeTakenToRun()) + " minutes")