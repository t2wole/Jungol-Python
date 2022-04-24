n = 0
sum = 0

while True:
    a = int(input())
    sum += a
    n += 1
    if a >= 100:
        break
print(sum)
print("%.1f" % (sum/n))

