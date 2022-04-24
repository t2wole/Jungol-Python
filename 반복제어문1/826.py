lst = ["Seoul", "Washington", "Tokyo", "Beijing"]

while True:
    print("""1. Korea
2. USA
3. Japan
4. China""")

    a = input("number? ")

    if 0 < int(a) <= len(lst):
        print(lst[int(a) - 1])

    else:
        print("none")
        break
