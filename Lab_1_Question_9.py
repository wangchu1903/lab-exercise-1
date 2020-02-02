count = int(input("Enter the count for sum"))
sumValue = 0
def sum(n):
    return (n * (n + 1)) / 2

for i in range(count):
    sumValue += sum(i)

print(sumValue)