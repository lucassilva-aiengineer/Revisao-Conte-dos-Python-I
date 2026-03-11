# Testando algumas ideias. 

from typing import List, Optional


def testando_erros_de_excecao()-> None:

    lista: List[Optional[str]] = []

    print(lista[0])


def encontrando_indice()-> List[int]:

    lista_nomes = ["Lucas", "Carlos", "Mateus"]

    # for nome in lista_nomes:
    #     indices.append(nome.index())

    return [lista_nomes.index(nome) for nome in lista_nomes]


def main():


    # testando_erros_de_excecao() 

    print(encontrando_indice())


if __name__ == '__main__':
    main()