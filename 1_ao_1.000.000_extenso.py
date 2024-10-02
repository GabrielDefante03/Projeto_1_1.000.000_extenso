# Listas com os números por extenso

unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos",
            "oitocentos", "novecentos"]
dezenas_especiais = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito",
                     "dezenove"]
u = int
d = int
c = int
um = int
dm = int
cm = int
x = int
saida = ""
# MENU QUE PERGUNTA SE QUER COMEÇAS O TESTE
contador = int(input("Vamos começar com os testes?\n1 - Sim\t\t\t - Não\t\n"))
print("\n__________________________________\n")
while (x != 0):
# VERIFICANDO SE ESTÁ CORRETA A INFORMAÇÃO DO LAÇO
    if(contador == 2):
        x = 0
    elif(contador < 1 or contador > 2):
        contador = int(input("Digite uma opção correta, por favor\n1 - Sim\t\t\t2 - Não\t\n"))
        print("\n__________________________________\n")
    else:
        numero = int(input("Digite um número entre 1 e 1.000.000: \n"))
        print("\n__________________________________\n")
        while(numero < 1 or numero > 1000000):
            numero = int(input("Escreva um número correto seu tontão \nEntre 1 e 1.000.000 \n"))
            print("\n__________________________________\n")
# de 1 a 10
    if (numero < 10):
        print("Seu número é:", unidades[numero])
        print("\n__________________________________\n")
# de 10 a 20
    elif (10 <= numero < 20):
        u = numero % 10
        print("Seu número é:", dezenas_especiais[u], "\n")
        print("\n__________________________________\n")
# de 20 a 100
    elif (20 <= numero < 100):
        d = numero // 10
        u = numero % 10
        if (u == 0):
            print("Seu número é:", dezenas[d])
        else:
            print("Seu número é:", dezenas[d], "e", unidades[u], "\n")
        print("\n__________________________________\n")
# se o número for 100
    elif (numero == 100) :
            print("Seu número é: cem\n")
            print("\n__________________________________\n")
# de 100 a 1000
    elif(100 < numero < 1000):
        c = (numero // 100) % 10
        d = (numero // 10) % 10
        u = numero % 10
        print(d)
        if (dezenas[d] == ""):
                print("Seu número é:", centenas[c], "e", unidades[u], "\n")
        elif (unidades[u] == ""):
                print("Seu número é:", centenas[c], "e", dezenas[d], "\n")
        else:
                print("Seu número é:", centenas[c], "e", dezenas[d], "e", unidades[u], "\n")
# de 1.000 a 10.000
    elif(1000 <= numero < 10000) :
        um = numero // 1000
        c = (numero // 100) % 10
        d = (numero // 10) % 10
        u = numero % 10
        if (um != 0 ):
            saida += unidades[um] + " mil "
        if (c > 1 ):
            saida += "" + centenas[c]
        if (c == 1 and d == 0 and u == 0):
            saida += "e " + "cem"
        if (d == 1 and u == 0):
            saida += " e " + dezenas_especiais[u]
        if (d  > 1 ):
            saida += " e " + dezenas[d]
        if (u != 0 and d > 1 or u != 0 and d == 0  or u != 0 and c == 0 and d > 1):
            saida += " e " + unidades[u]
        print(saida,"\n")
        print("\n__________________________________\n")
# de 10.000 a 100.000
    elif (10000 <= numero < 100000):
        dm = numero // 10000
        um = (numero // 1000) % 10
        c = (numero // 100) % 10
        d = (numero // 10) % 10
        u = numero % 10
        if (dm == 1):
            saida += dezenas_especiais[um] + " mil "
        if (d > 1):
            saida += dezenas[dm] + " mil "
        if (um != 0 ):
            saida += unidades[um] + " mil "
        if (c > 1 ):
            saida += "" + centenas[c]
        if (c == 1 and d == 0 and u == 0):
            saida += "e " + "cem"
        if (d == 1 and u == 0):
            saida += " e " + dezenas_especiais[u]
        if (d  > 1 ):
            saida += " e " + dezenas[d]
        if (u != 0 and d > 1 or u != 0 and d == 0  or u != 0 and c == 0 and d > 1):
            saida += " e " + unidades[u]
        print(saida, "\n")
        print("\n__________________________________\n")
# de 100.000 a 1.000.000
    else:
        cm = numero // 100000
        dm = (numero // 10000) % 10
        um = (numero // 1000) % 10
        c = (numero // 100) % 10
        d = (numero // 10) % 10
        u = numero % 10
        if (cm != 0):
            saida += centenas[cm] + ""
            if (dm == 0 and um == 0):
                saida += " mil "
        if (dm == 1):
            saida += " e " + dezenas_especiais[um] + " mil "
        if (d > 1):
            saida += " e " + dezenas[dm]
        if (um != 0 and d > 1 or um != 0 and cm != 0):
            saida += " e " + unidades[um] + " mil "
        if (c != 0):
            saida += "" + centenas[c]
        if (d == 1):
            saida += " e " + dezenas_especiais[u]
        if (d > 1):
            saida += " e " + dezenas[d]
        if (u != 0 and d > 1 or u != 0 and d != 0):
            saida += " e " + unidades[u]
        print(saida, "\n")
        print("\n__________________________________\n")
#MENU QUE PERGUNTA SE QUER COMEÇAS O TESTE
    contador = int(input("Quer continuar os testes?\n1 - Sim\t\t\t2 - Não\t\n"))
    print("\n__________________________________\n")
    if (x != 0):
# VERIFICANDO SE ESTÁ CORRETA A INFORMAÇÃO DO LAÇO
        if (contador == 2):
            x = 0
        elif (contador < 1 or contador > 2):
            contador = int(input("Digite uma opção correta, por favor\n1 - Sim\t\t\t2 - Não\t\n"))
            print("\n__________________________________\n")

    saida = ""
