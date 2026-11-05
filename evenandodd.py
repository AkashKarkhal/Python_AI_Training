counteven = 0
sumeven = 0
countodd = 0
sumodd = 0

for i in range(1, 50):
    if i % 2 == 0:
        sumeven += i
        counteven += 1
        print("Even numbers are ", i)
    else:
        sumodd += i
        countodd += 1
        print("odd numbers are ", i)


print("Even Count:", counteven)
print("Even Sum:", sumeven)

print("Odd Count:", countodd)
print("Odd Sum:", sumodd)


