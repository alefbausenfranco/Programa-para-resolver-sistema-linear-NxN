import math
controle = 0
matriz = []
b = []
x = []
n = 0

# inicio das funções

def menu():
    global matriz, b, x, controle, n
    print('\nCALCULO DE SISTEMA LINEAR')
    print('''    [1] Ler Matriz e vetor A
    [2] Imprimir na tela o sistema Ax=B
    [3] Resolver o sistema Ax=B
    [4] Sair
    ''')
    opcao = 0
    while opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4':
        opcao = input('Digite sua opção (1/2/3/4): ')
        if opcao == '1' and controle >= 0:
            controle = 1
            matriz, b, x = menu1()
            menu()

        elif opcao == '2' and controle >= 1:
            menu2(1)
            controle = 2
            menu()
        elif opcao == '2' and controle == 0:
            menu2(0)
            menu()
        elif opcao == '3' and controle == 2:
            print('A solução para o seu sistema é \n')
            gauss(matriz, b)
            menu()

        elif opcao == '4':
            print('Você encerrou o programa')


        elif not(opcao in['1', '2', '3', '4']):
            print('\nOpção inválida')


        else:
            print('\n Você cometeu um equívoco, o programa funciona em etapas, passe pelos menus 1 e 2')
            opcao = 0
            menu()

def menu1():
    #Ler a matriz do usuário
    global matriz, b, x, n
    # Matriz A
    opcao = '0'
    while opcao != '1':
        # Digitar matriz A
        matriz = []
        n = int(input("Qual o número de variáveis? (Apenas números): "))
        print('\nDigite a matriz A (Apenas números)')
        for i in range(n):
            linha = []
            for j in range(n):
                print("Qual o elemento da coluna", j + 1, "da linha", i + 1, ": ")
                linha.append(float("{:.2f}".format(float(input()))))
            matriz.append(linha)
        # mostrar matriz
        print('A =')
        for l in range(0, n):
            for c in range(0, n):
                print(f'[{matriz[l][c]:^5.2f}]', end='')
            print()
        opcao = input('\nConfirmar matriz A? (Sim = 1, Refazer = 0): ')

    # Matriz B
    opcaob = '0'
    while opcaob != '1':
        # Digitar matriz
        b = []
        print('\nDigite a matriz B')
        for i in range(1, n + 1):
            print('Qual o valor do elemento da linha', i, '? (Apenas números):', )
            b.append((float(input())))
            i += 1

        # mostrar matriz
        print('B =')
        for l in range(0, n):
            print(f'[{b[l]:^5.2f}]', end='')
            print()
        opcaob = input('\nConfirmar matriz B? (Sim = 1, Refazer = 0): ')

    # matriz x
    x = []
    for i in range(1, n + 1):
        x.append(f'x{i}')
    return matriz, b, x


def menu2(a):
    #Mostrar o sistema ax=b
    global matriz, b, x, n

    if a == 1:
        tamanho_a = 6

        for linha in matriz:
            linha = [abs(ele) for ele in linha]
            if math.ceil(math.log(max(linha), 10)) > (tamanho_a - 5):
                tamanho_a = (math.ceil(math.log(max(linha), 10)) + 5)

        tamanho_b = [abs(ele) for ele in b]
        tamanho_b = (math.ceil(math.log(max(tamanho_b), 10))) + 5

        letra = 'A'
        print(f'{letra:^{(tamanho_a * n) + 2}}', end='')

        print(f'       x      ', end='')
        letra = 'B'
        print(f'{letra:^{tamanho_b + 2}}')

        for i in range(n):
            print(f'[', end='')
            for j in range(n):
                if j == (n - 1):
                    print(f'{matriz[i][j]:^{tamanho_a}.2f}]', end='')
                else:
                    print(f'{matriz[i][j]:^{tamanho_a}.2f}', end='')

            if i == math.floor(n / 2):
                print(f'  X  [x{i + 1}]  =  [{b[i]:^{tamanho_b}.2f}]', end='')
            else:
                print(f'     [x{i + 1}]     [{b[i]:^{tamanho_b}.2f}]', end='')
            print()

    elif a == 0:
        print('\nSeu sistema Ax=B ')
        q = [0]
        w = [0]
        e = [0]
        print(f'{q},{w},{e}')


def gauss(a, b):
    #Calcular e mostrar o valor das variáveis

    # pivoteamento
    global n
    for k in range(n):
        pivo = a[k][k]
        l_pivo = k
        for i in range(k + 1, n):
            if (abs(a[i][k]) > abs(pivo)):
                pivo = a[i][k]
                l_pivo = i
        if pivo == 0:
            print("A matriz é singular.")
            break
        if l_pivo != k:
            for j in range(n):
                troca = a[k][j]
                a[k][j] = a[l_pivo][j]
                a[l_pivo][j] = troca
            troca = b[k]
            b[k] = b[l_pivo]
            b[l_pivo] = troca
        for i in range(k + 1, n):
            m = a[i][k] / a[k][k]
            a[i][k] = 0
            for j in range(k + 1, n):
                a[i][j] = a[i][j] - (m * a[k][j])
            b[i] = b[i] - (m * b[k])

    #Verificando se o determinante da diagonal principal é 0, ou se a última linha é 0
    for i in range(n):
        if round(a[i][i], ndigits=6) == 0:
            print(f'\nA matriz informada tem determinante igual a 0, portanto, não tem solução ou tem infinitas soluções.')
            return

    #Mostrar resultados
    resolucao = [0] * n
    resolucao[n - 1] = (b[n - 1] / a[n - 1][n - 1])
    for k in range(n - 2, -1, -1):
        s = 0
        for j in range((k + 1), n):
            s = s + a[k][j] * resolucao[j]
        resolucao[k] = ((b[k] - s) / a[k][k])

    for i in range(n):
        print(f'x{i+1} = {resolucao[i]:.2f}')

# Fim das funções

menu()
