sum = 0
n = int(input())

while True:
    sum += n
    n -= 1
    if(n == 0):
        break
print(sum)

