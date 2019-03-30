i = 1
n = int(input("Repeat count? "))

while i <= n:
    if i % 2 == 0:
        print(i)
    else:
        print("###")
    i += 1