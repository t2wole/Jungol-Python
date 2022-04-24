def function(a, b, c):
    if b == "+":
        print("%d + %d = %d" % (a, c, a+c))
    elif b == "-":
        print("%d - %d = %d" % (a, c, a-c))
    elif b == "*":
        print("%d * %d = %d" % (a, c, a*c))
    elif b == "/":
        print("%d / %d = %d" % (a, c, a//c))

str = input().split()
function(int(str[0]), str[1], int(str[2]))