def function(a, b):
    if a > b:
        a = a // 2
        b = b * 2
    elif b > a:
        b = b // 2
        a = a * 2
    lst.append(a)
    lst.append(b)
    return lst

a, b = input().split()
a = int(a)
b = int(b)
lst = []

lst = function(a, b)

print("%d %d" % (lst[0], lst[1]))


