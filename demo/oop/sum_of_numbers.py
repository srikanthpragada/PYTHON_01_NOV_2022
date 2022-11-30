
total = 0
for i in range(5):
    try:
        n = int(input("Enter number :"))
        total += n
    except ValueError:
        print("Invalid Number")


print(total)

