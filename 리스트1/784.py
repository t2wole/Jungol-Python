b = int(input())
a = [1, 2]
a.append(b)

for i in range(len(a)-1, -1, -1):
    print(a[i])

