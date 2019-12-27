s = ""
a = 3

while a != 1:
    s = s + str(a)
    if a % 2 == 0:
        a = a / 2
    else:
        a = 3 * a + 1
    a = int(a)
    print(s)
    print(a)
    print()
