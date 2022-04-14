def geradorTabelaVerdade (lista):
    #verifica num de variaveis na lista enviada
    numVariaveis = len(lista)
    #2³ = 8, 8 resultados, onde 3 é o numero de variaveis.
    resultados = pow(2, numVariaveis)
    #guarda o resultados para ser usado n duplicaçao
    hold_resultados_originais = pow(2, numVariaveis)
    #holder de valores
    verdadeiro = "True"
    falso = "False"

    for elementos in lista:
        #cria variaveis com o nome das variaveis digitados
        globals()[elementos] = []

        #somente a 1 variavel da lista (nao precisa duplicar, pq é um conjunto unico)
        if lista[0] == elementos:
            #aplica verdadeiro no primeiro
            for index in range(0, int(resultados / 2), 1):
                eval(elementos).append("True")
            #aplica falso no primeiro
            for index in range(int(resultados / 2), resultados, 1):
                eval(elementos).append("False")
            #descartar combinações ja usadas
            resultados = int(resultados / 2)

        #variaveis restantes (precisa duplicar pq sao conjuntos repetidos)
        else:
            #aplica verdadeiro no primeiro
            for index in range(0, int(resultados / 2), 1):
                eval(elementos).append("True")
            #aplica falso no primeiro
            for index in range(int(resultados / 2), resultados, 1):
                eval(elementos).append("False")
            #duplica ate ficar com o mesmo numero de resultados que precisa
            while len(eval(elementos)) < hold_resultados_originais:
                eval(elementos).extend(eval(elementos))
            #descartar combinações ja usadas
            resultados = int(resultados / 2)
        


teste = ["p", "q", "r", "s"]
geradorTabelaVerdade(teste)
print(p)
print(q)
print(r)
print(s)