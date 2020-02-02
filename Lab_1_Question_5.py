import math

one = int(input("Number of students in class one"))
two = int(input("Number of students in class two"))
three = int(input("Number of students in class three"))

NUMBER_OF_STUDENTS_IN_ONE_DESK = 2

def calculateNumberOfDesk(numberOfStudents):
    return math.ceil((numberOfStudents / NUMBER_OF_STUDENTS_IN_ONE_DESK))

classOne = calculateNumberOfDesk(one)
classTwo = calculateNumberOfDesk(two)
classThree = calculateNumberOfDesk(three)
print(classOne)
print(classTwo)
print(classThree)

print("total desk = " + str(classOne + classTwo + classThree))