import random 

# Removendo elementos 


def main():

    lista = ["Marcos", "João", "José", "Junior"]

    def remover_item()-> None:
        item_removido = lista.pop()

        print(item_removido)

    # remover_item() 

    # print(lista)


    lista.reverse()

    # print(lista)

    # Ordenando valores. 

    lista_numeros = [10, 15, 5, 2, 3, 8, 9]

    lista_numeros.sort() # Altera a lista original 

    # print(lista_numeros) 

    nova_lista = [0] * 100  

    # print(nova_lista[:5]) 

    lista_numerica = [random.randint(0, 100)] * 100

    # print(lista_numerica[:20])

    listas_concatenadas = lista_numeros + lista_numerica

    # print(listas_concatenadas)  

    # fatiamento em listas 

    sub_lista_a = listas_concatenadas[1:10]
    sub_lista_b = listas_concatenadas[: 80] # de um ao índice 4. 
    sub_lista_c = listas_concatenadas[10: ]

    # print(sub_lista_a) 

    # É possível alterar os passos percorridos. 

    print(sub_lista_b[1:20:2])  # percorrendo do índice zero até ao índice 19  
                                # saltando de dois em dois. 

    def teste_rapido():

        indice = 0
        for n in sub_lista_b:
            print("indice: ", indice, "numero: ", sub_lista_b[indice])
            indice += 1


    def copiando_lista():

        lista_palavras = ["Mesa", "Casa", "Carro"]

        copia = lista_palavras[:]
        copia_a = list(lista_palavras)

        lista_b = lista_palavras.copy()

        # print(lista_b)

        lista_b.remove("Casa")
        print(lista_palavras)

        print(lista_b)

        # Trocando item por meio do índice. 

        lista_palavras[2] = "Pessoa"

        lista_palavras.insert(1, "Avião")

        print(lista_palavras)


        numeros_aleatorios = [random.randint(0, 40) for numero in range(0, 10)]

        print(numeros_aleatorios)

    copiando_lista()


if __name__ == "__main__":
    main()