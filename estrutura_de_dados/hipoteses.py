# Testando algumas ideias. 

from typing import List, Optional


def testando_erros_de_excecao()-> None:

    lista: List[Optional[str]] = []

    print(lista[0])

def main():


    testando_erros_de_excecao()


if __name__ == '__main__':
    main()