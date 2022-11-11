l1 = [10, 20, 30, 40, 50, 60]
l2 = ['abc', 'xyz', 'pqr']
extra_values = ['None'] * (len(l1) - len(l2))
l2 += extra_values
for fv, sv in zip(l1, l2):
    print(fv, sv)


