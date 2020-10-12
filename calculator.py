#Funcao de boas vindas ao user
def boasvindas():
    print('''
    Bem Vindo User!
    ''')

def calcular():
    operation = input('''
        Por favor indique o tipo de operação que deseja através dos seguintes caracteres :
        + , - ,  * , / , ** ou %
        ''')

    #Pedido dos valores para efetuar a operação 
    valor1 = float( input("Insira um valor: ") )
    valor2 = float( input("Insira mais um valor: ") )


    if operation == '+':
        # Soma
        soma = valor1 + valor2
        print(valor1,'+',valor2,' = ' , soma)

    elif operation == '-':
        # Subtracao
        subtracao = valor1 - valor2
        print(valor1,'-',valor2,' = ' , subtracao)

    elif operation == '*':
        # Multiplicacao
        multi = valor1 * valor2
        print(valor1,'*',valor2,' = ' , multi)

    elif operation == '/':
        # Divisao
        div = valor1 / valor2
        print(valor1,'/',valor2,' = ' , div)

    elif operation == '**':
        # Calcular numeros exponenciais
        expo = valor1 ** valor2
        print(valor1,'**',valor2,' = ' , expo)

    elif operation == '%':
        # Calcula o resto da divisao
        resto = valor1 % valor2
        print(valor1,'%',valor2,' = ' , resto)

    else:
        print('O operador escolhido é inválido')

    recalcular()

def recalcular():
    calcular_novamente = input('''
        Deseja efetuar uma nova operação? 
        Se sim, digite 'Y', se não, digite 'N'
        ''')

    if calcular_novamente == 'Y':
        calcular()

    elif calcular_novamente == 'N':
        print('Até Breve!:)')

    else:
        recalcular()

boasvindas()
calcular()


