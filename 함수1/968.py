def function():
    a = list(map(int, input().split()))
    for i in range(min(a), max(a) + 1):
        print("== %ddan ==" % i)

        for j in range(1, 10):
            if i * j < 10:
                print("%d * %d =  %d" % (i, j, i*j))
            else:
                print("%d * %d = %d" % (i, j, i*j))
        print()
function()