# Factorial function
def fact(num):
    if num <= 1:
        return 1
    return num*fact(num-1)


def exponential_series(num, x=2):
    sum = 0
    for i in range(0,num):
        sum = sum + (x**i) / (fact(i))
    print("The exponential maclaurin series for {} is {}".format('e^x',sum))

def cosine_series(num,x):
    sum = 0
    sign = 1
    for i in range(0,num):
        sum = sum + sign*(x**(i*2)) / (fact(i*2))
        sign *= (-1)
    print("The cosine maclaurin series for {} is {}".format('cos(x)',sum))

def sinine_series(num,x):
    sum = 0
    sign = 1
    for i in range(1,num):
        sum = sum + sign*(x**(2*i-1)) / (fact(2*i-1))
        sign *= (-1)
    print("The sinine maclaurin series for {} is {}".format('sin(x)',sum))
    

def main():
    type = str(input('Enter cos or sin or e^x:'))
    if type == 'cos':
        x = int(input('Enter x: '))
        n = int(input('Enter n: '))
        cosine_series(n,x)
    elif type =='sin':
        x = int(input('Enter x: '))
        n = int(input('Enter n: '))
        sinine_series(n,x)
    else:
        n = int(input('Enter n: '))
        exponential_series(n)
main()