#Calculadora v0.1 (Calculadora simples)

num1 = int(input('Insira primeiro numero: '))

num2 = int(input('Insira segundo numero: '))

decisao = int(input('Qual operação você deseja realizar?\n' + 
'1 - Soma, 2 - Subtrair, 3 - Multi, 4 - Div\n'))

def function_Plus(num1, num2):
    return num1 + num2

def function_Minus(num1, num2):
    return num1 - num2

def function_Multi(num1, num2):
    return num1 * num2

def function_Div(num1, num2):
    return num1 / num2

match decisao:
    case 1:
        result = function_Plus(num1, num2)
        print(result)
    case 2:
        result = function_Minus(num1, num2)
        print(result)
    case 3:
        result = function_Multi(num1, num2)
        print(result)
    case 4:
        result = function_Div(num1, num2)
        print(result)

