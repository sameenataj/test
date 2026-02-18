
def get_number(num):
    while True:
        operand = input(f"Number {num}: ")
        try :
            return float(operand)            
        except:
            print('Invalid number, try again')

operand1 = get_number('1')
operand2 = get_number('2')

valid = True
sign = input("Sign: ")

expression = str(operand1) + sign + str(operand2)

if(valid):
    print (expression)

    if(sign == '+'):
        result = operand1 + operand2
    elif (sign == '-'):
        result = operand1 - operand2
    elif (sign == '*'):
        result = operand1 * (operand2)
    elif (sign == '/'):
        if((operand2)!=0):
            result = (operand1) / (operand2)
        else:
            result = 'invalid operation' 
    elif (sign == "**"):
        result = (operand1) ** (operand2)
    elif (sign == "%"):
        if((operand2)!=0):
            result = (operand1) % (operand2)
        else:
            result = 'invalid operation:division by zero'    
    else:
        result = 'invalid operation'
    print (result)