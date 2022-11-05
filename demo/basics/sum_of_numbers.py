# Take numbers until 0 is given and display total for numbers
total = 0
while True:
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break
    total = total + num

print("Total = ", total)