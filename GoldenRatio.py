
x = 0
y = 1

for i in range(20000):
    print(x)
    print(y)
    x += y
    y += x

z = y/x

print('The golden ratio is ' + str(z) + '.')
