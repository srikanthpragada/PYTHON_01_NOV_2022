# Take numbers until 0 is given and display avg for numbers
total = count = 0
while True:
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break

    if num < 0:
        continue

    total = total + num
    count += 1

print("Average  = ", total // count)