import math

def intdetector(x1):
    y1 = int(x1)

    z1 = x1 / y1

    if z1 == 1:
        return(True)
    else:
        return(False)
    
while True:
    try:
        a = input('a: ')
        if a == 'exit':
            print('Exiting...')
            break
        b = input('b: ')
        if b == 'exit':
            print('Exiting...')
            break
        c = input('c: ')
        if c == 'exit':
            print('Exiting...')
            break

        a = int(a)
        b = int(b)
        c = int(c)
            
        x = (-4) * a * c
        y = 2 * a
        z = (-1) * b
        u = b ** 2
        n = u + x
        m = math.sqrt(n)

        d = z + m
        f = z - m

        sol1 = d / y
        sol2 = f / y

        if intdetector(m):
            if sol1 == sol2:
                if intdetector(sol1):
                    print('The answer is double ' + str(int(sol1)) + '.')
                else:
                    print('The answer is double ' + str(int(d)) + '/' + str(int(y) + '.'))
            else:
                if intdetector(sol1):
                    if intdetector(sol2):
                        print('The answers are ' + str(int(sol1)) + ' and ' + str(int(sol2)) + '.')
                    else:
                        print('The answers are ' + str(int(sol1)) + ' and ' + str(int(f)) + '/' + str(int(y)) + '.')
                else:
                    if intdetector(sol2):
                        print('The answers are ' + str(int(d)) + '/' + str(int(y)) + ' and ' + str(int(sol2)) + '.')
                    else:
                        print('The answers are ' + str(int(d)) + '/' + str(int(y)) + ' and ' + str(int(f)) + '/' + str(int(y)) + '.')
        else:
            print('The answer involves a square root with a float result.')
    except ValueError:
        print('The answer is an imaginary number.')
    except:
        print('Something went wrong!')
        print('Exiting...')
        break
