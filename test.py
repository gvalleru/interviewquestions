from collections import Counter

x = [1, 0, 3]
print all(x)
print any(x)

x = [x for x in range(10) if x % 2 == 0]
print x

x = (x for x in range(10) if x % 2 == 0)
print x

print sum(x)

a = Counter("gopi")
b = Counter("bobo")
print a, b

for i,j in a.items():
    print i, j

print (a + b)
print (a + b).most_common(3)

len()

