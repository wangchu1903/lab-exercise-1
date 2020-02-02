students = int(input("number of students"))
apples = int(input("number of apples"))

def appleForEachStudent(student, apples):
    return apples / student

def remainingApples(student, appleForEachStudent):
    return (student * appleForEachStudent) - apples

numberOfApplesForEachStudent = appleForEachStudent(students, apples)
print("Every student will receive "+str(numberOfApplesForEachStudent) + " apples")

print("Remaining apple in basket is " + str(remainingApples(students, numberOfApplesForEachStudent)))
