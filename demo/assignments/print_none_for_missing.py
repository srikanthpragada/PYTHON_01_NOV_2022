
l1 = [10, 20, 30, 40, 50, 60]
l2 = ['abc', 'xyz', 'pqr']
for idx, fv in enumerate(l1):
    if idx < len(l2):
        print(fv, l2[idx])
    else:
        print(fv, 'None')
