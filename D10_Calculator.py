def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {'+': add, '-': sub, '*': multiply, '/': divide}

n1= float(input('pick the first number: '))
continue_cal = True

while continue_cal:
    Operation = input('pick an operation: ') 
    n2= float(input('pick the second number: '))
    
    if Operation not in operations:
        print("Invalid operator")
        continue

    ans = (operations[Operation](n1,n2))
    print(f'{n1} {Operation} {n2} = {ans}')

    continue_cal = input('continue using previous results?: ').lower()
    if continue_cal == 'yes':
        n1 = ans
    else:
        continue_cal = False

print(f'{n1} {Operation} {n2} = {ans}')
    