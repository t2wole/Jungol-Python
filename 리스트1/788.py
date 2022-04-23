a = list(range(1, 16))
n = int(input())
lst = []

for i in a:
    if i % n == 0: 
        lst.append(i)
print(lst)

