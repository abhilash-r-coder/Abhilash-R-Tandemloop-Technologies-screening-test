a = int(input("Enter a: "))

result = []
num = 1

for i in range(a):
    result.append(num)
    num += 2

print(", ".join(map(str, result)))
