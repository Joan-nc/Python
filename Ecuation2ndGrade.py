import math
import fractions

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

        if a == '' or b == '' or c == '':
            print('You must fill all variables.')
        else:
            a = int(a)
            b = int(b)
            c = int(c)

            if a == 0:
                if b == 0:
                    print('There is no solution.')
                elif c == 0:
                    print('The answer is 0.')
                else:
                    x2 = (-1) * c
                    y2 = x2 / b
                    print('The solution is ' + str(fractions.Fraction(y2)) + '.')
            elif b == 0:
                if c == 0:
                    print('The answer is double 0.')
                else:
                    x3 = (-1) * c
                    y3 = x3 / a
                    z3 = math.sqrt(y3)
                    print('The answers are ' + str(fractions.Fraction(z3)) + ' and -' + str(fractions.Fraction(z3)) + '.')
            elif c == 0:
                x4 = (-1) * b
                y4 = x4 / a
                print('The answers are 0 and ' + str(fractions.Fraction(y4)) + '.')
            else:
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

                if int(m) == m:
                    if sol1 == sol2:
                        print('The answer is double ' + str(fraction.Fraction(sol1)) + '.')
                    else:
                        print('The answers are ' + str(fractions.Fraction(sol1)) + ' and ' + str(fractions.Fraction(sol2)) + '.')
                else:
                    print('The answers are ' + str(z) + ' + square root of ' + str(n) + '/' + str(y) + ' and ' + str(z) + ' - square root of ' + str(n) + '/' + str(y) +'.')
            
            
    except ValueError:
        print('The answer is an imaginary number.')
    except:
        print('Something went wrong!')
        print('Exiting...')
        break
