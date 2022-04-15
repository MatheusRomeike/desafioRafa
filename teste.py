def geradorTabelaVerdade(lista):
    # verifica num de variaveis na lista enviada
    numVariaveis = len(lista)
    # 2³ = 8, 8 resultados, onde 3 é o numero de variaveis.
    resultados = pow(2, numVariaveis)
    # guarda o resultados para ser usado n duplicaçao
    global hold_resultados_originais
    hold_resultados_originais = pow(2, numVariaveis)

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
            while len(eval(elementos)) < hold_resultados_originais:
                eval(elementos).extend(eval(elementos))
            # descartar combinações ja usadas
            resultados = int(resultados / 2)


def realizadorDeOperacoes(variavel1, operacao, variavel2, listaParaResultado):
    for pos in range(0, hold_resultados_originais, 1):
        # operacao com E
        if operacao == "&":
            # colocar valores na variavel final depois de fazer a logica
            logica = variavel1[pos] and variavel2[pos]
            listaParaResultado.append(logica)
         # operacao com OU
        elif operacao == "v":
            # colocar valores na variavel final depois de fazer a logica
            logica = variavel1[pos] or variavel2[pos]
            listaParaResultado.append(logica)
        # operacao com IMPLICACAO
        elif operacao == ">":
            # colocar valores na variavel final depois de fazer a logica
            logica = variavel1[pos] <= variavel2[pos]
            listaParaResultado.append(logica)
        # operacao com BICONDICIONAL
        else:
            # colocar valores na variavel final depois de fazer a logica
            logica = variavel1[pos] == variavel2[pos]
            listaParaResultado.append(logica)


def separadorDeVariaveis(expressao):
    lista_variavel = []

    for element in expressao:
        # tudo que nao for operador ou parenteses é contado como variavel, uma vez
        if (element != "&") and (element != "v") and (element != ">") and (element != "-") and (element != "(") and (element != ")") and (element not in lista_variavel):
            lista_variavel.append(element)
                
    return lista_variavel


lista_resultado = []
expressaoteste = input("Insira a expressao: ")

geradorTabelaVerdade(separadorDeVariaveis(expressaoteste))

realizadorDeOperacoes(p, ">", q, lista_resultado)
print(lista_resultado)

#Falta fazer o check de parenteses e ordem de precedencia