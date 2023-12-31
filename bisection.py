# Pendefinisian fungsi
def f(x):
    return x**3-5*x-9

# Implementing Bisection Method
def bisection(x0,x1,e):
    step = 1
    print('\n\n*** IMPLEMNTASI METODE BISEKSI ***')
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        step = step + 1
        condition = abs(f(x2)) > e

    print('\nAkar dari persamaan tersebut : %0.8f' % x2)


# Input Section
x0 = input('Titik X0 : ')
x1 = input('Titik X1 : ')
e = input('Error toleransi : ')

# Converting input to float
x0 = float(x0)
x1 = float(x1)
e = float(e)


# Check nilai fungsi
if f(x0) * f(x1) > 0.0:
    print('di antara dua titik tidak terdapat akar .')
    print('masukan nilai baru.')
else:
    bisection(x0,x1,e)
