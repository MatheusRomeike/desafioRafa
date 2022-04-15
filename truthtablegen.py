# 1
def geradorTabelaVerdade(lista):
    # verifica num de variaveis na lista enviada
    numVariaveis = len(lista)
    # 2³ = 8, 8 resultados, onde 3 é o numero de variaveis.
    resultados = pow(2, numVariaveis)
    # guarda o resultados para ser usado n duplicaçao
    hold_vari_quadrado = pow(2, numVariaveis)

    for elementos in lista:
        # cria variaveis com o nome das variaveis digitados
        globals()[elementos] = []

        # somente a 1 variavel da lista (nao precisa duplicar, pq é um conjunto unico)
        if lista[0] == elementos:
            # aplica verdadeiro no primeiro
            for index in range(0, int(resultados / 2), 1):
                eval(elementos).append(True)
            # aplica falso no primeiro
            for index in range(int(resultados / 2), resultados, 1):
                eval(elementos).append(False)
            # descartar combinações ja usadas
            resultados = int(resultados / 2)

        # variaveis restantes (precisa duplicar pq sao conjuntos repetidos)
        else:
            # aplica verdadeiro no primeiro
            for index in range(0, int(resultados / 2), 1):
                eval(elementos).append(True)
            # aplica falso no primeiro
            for index in range(int(resultados / 2), resultados, 1):
                eval(elementos).append(False)
            # duplica ate ficar com o mesmo numero de resultados que precisa
            while len(eval(elementos)) < hold_vari_quadrado:
                eval(elementos).extend(eval(elementos))
            # descartar combinações ja usadas
            resultados = int(resultados / 2)
    return hold_vari_quadrado

# 2


def separadorDeVariaveis(expressao):
    lista_variavel = []

    for element in expressao:
        # tudo que nao for operador ou parenteses é contado como variavel, uma vez
        if (element != "&") and (element != "|") and (element != "<") and (element != "=") and (element != "(") and (element != ")") and (element not in lista_variavel):
            lista_variavel.append(element)

    return lista_variavel

# 3


def resolverExpressao(expressao, num_vari):
    alfabeto = []
    # cria a lista alfabeto q vai ser percorrida preenchendo
    for element in expressao:
        # tudo que nao for operador ou parenteses é contado como variavel, uma vez
        if (element != "&") and (element != "|") and (element != "<") and (element != "=") and (element != "(") and (element != ")") and (element not in alfabeto):
            alfabeto.append(element)
    nova_expressao = expressao

    # percorre a expressao preenchendo [pos] nas variaveis
    for letra in alfabeto:
        nova_expressao = nova_expressao.replace(letra, letra+"[ç]")
    print(nova_expressao)
    resultado = []
    # resolver a expressao agr
    for ç in range(0, num_vari, 1):
        resultado.append(eval(nova_expressao))

    print(resultado)


print("Bem vindo, use variaveis minusculas de a-z, menos o ç. \nPara usar o operador E, utilize &. \nPara usar o operador OU, utilize |. \nPara usar o operador IMPLICANCIA, utilize <=. \nPara usar o operador BICONDICIONAL, utilize ==.")

#expressaoteste = "a==(b|(c&(d|(f<=(g==(h&(k|(l|(m&n)))))))))"

expressao_digitada = input("Informe a expressao a ser calculada: ")


variaveis_ao_quadrado = geradorTabelaVerdade(
    separadorDeVariaveis(expressao_digitada))
resolverExpressao(expressao_digitada, variaveis_ao_quadrado)
