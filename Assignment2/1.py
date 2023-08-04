#############Q1#########################
res1 = []

for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        res1.append(num)

print(','.join(map(str, res1)))