# define Python user-defined exceptions
class InvalidOptionException(Exception):
    "Raised when the input value is not [cos, sin, e^x] "
    pass


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
    while True:
        try:
            type = str(input('Enter cos or sin or e^x:'))
            if type not in ["cos", "sin", "e^x"]:
                raise InvalidOptionException()
            break
        except InvalidOptionException:
            print("please enter a valid option such as cos or sin or e^x")
        except ValueError:
            print("please enter a valid string")
    if type == 'cos':
        while True:
            try:
                x = int(input('Enter x: '))
                n = int(input('Enter n: '))
                break
            except ValueError:
                print("please enter a valid number for n and x")
        cosine_series(n,x)
    elif type =='sin':
        while True:
            try:
                x = int(input('Enter x: '))
                n = int(input('Enter n: '))
                break
            except ValueError:
                print("please enter a valid number for n and x")
        sinine_series(n,x)
    else:
        while True:
            try:
                n = int(input('Enter n: '))
                break
            except ValueError:
                print("please enter a valid number for n")
        exponential_series(n)
main()