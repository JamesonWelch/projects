import math

def add():
    # Addition Operation
    a1 = float(input('Addition. Enter first number: '))
    a2 = float(input('Addition. Enter second number: '))
    a3 = a1 + a2
    print(a1, '+ ', a2, '=', a3)

def sub():
    # Subtracrtion Operation
    s1 = float(input('Subtraction. Enter first number: '))
    s2 = float(input('Subtraction. Enter second number: '))
    s3 = s1 - s2
    print(s1, '- ', s2, '=', s3)


# Multiplication Operation
def mul():
    m1 = float(input('Multiplication. Enter first number: '))
    m2 = float(input('Multiplication. Enter second number: '))
    m3 = m1 * m2
    print(m1, '* ', m2, '=', m3)

# Division Operation
def div():
    d1 = float(input('Division. Enter first number to be divided: '))
    d2 = float(input('Division. Enter second number to divide by: '))
    d3 = d1 / d2
    print(d1, 'divided by ', d2, '=', d3)

# Modulus Operation
def mod():
    mo1 = float(input('Modulus. Enter first number to be divided: '))
    mo2 = float(input('Modulus. Enter second number to divide by: '))
    mo3 = mo1 % mo2
    print('The modulus of ', mo1, 'divided by ', mo2, '=', mo3)

# Square Root Operation
def sqr():
    sqr1 = float(input('Square Root. Enter a number to find the square root: '))
    sqr2 = math.sqrt(sqr1)
    print('The square root of ', sqr1, '=', sqr2)

#Exponential Operation
def exp():
    exp1 = float(input('Exponentiation. Enter first number to be the base number: '))
    exp2 = float(input('Exponentiation. Enter second number to be the exponent: '))
    exp3 = exp1 ** exp2
    print(exp1, 'raised to the power of ', exp2, '=', exp3)

# Basic Triginometry Operation: sin(), cos(), tan()
# Showing results both in radians and degrees
def tri():
    rad = float(input("Trigonometry. Enter number to compute sine, cosine, and tangent: "))
    print('Sine: ', math.sin(rad), '°')
    print('Sine: ', (math.sin(math.radians(rad))), ' radians')
    print('Cosine: ', math.cos(rad), '°')
    print('Cosine: ', (math.cos(math.radians(rad))), ' radians')
    print('Tangent: ', math.tan(rad), '°')
    print('Tangent: ', (math.tan(math.radians(rad))), ' radians')

#Logarithm Operation
def log():
    log_x = float(input('Logarithm. Enter value of x: '))
    log_base = float(input('Enter the base number: '))
    log3 = math.log(log_x, log_base)
    print('Logarithm base ', log_base, ' of ', log_x, ' is ', log3)
    print('The natural log base e of ', log_x, ' is: ', math.log(log_x))
    print('The log base 10 of ', log_x, ' is: ', math.log10(log_x))

def run_all():
    add()
    sub()
    mul()
    div()
    mod()
    sqr()
    exp()
    tri()
    log()


dispatcher = {'a': add, 'b': sub, 'c': mul, 'd': div, 'e': mod,
              'f': sqr, 'g': exp, 'h': tri, 'i': log, 'x': run_all}

usr_input = input('Make a selection for a math function: \n'
                  '(a) for addition. \n(b) for subtraction. \n(c) for multiplication. \n'
                  '(d) for division. \n(e) for modulus. \n(f) for square root. \n'
                  '(g) for exponentiation. \n(h) for trigonometry. \n(i) for logirithm. \n'
                  '(x) for all functions. \n> ')

def fire(func):
    return func()

fire(dispatcher[usr_input])
