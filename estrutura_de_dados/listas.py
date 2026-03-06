from faker import Faker 
from typing import List 
import time
# Listas 

# faker = Faker('pt_BR') 


def manipulando_lista():
    faker = Faker('en_US')

    lista_nomes = [faker.name() for _ in range(10)]


    def imprimir_nomes():
        for nome in lista_nomes:
            print(nome)


def minha_lista():

    lista_pessoas = ["Mateus", "Marcos", "Lucas", "João"]

    tamanho_lista = len(lista_pessoas)

    def acessando_nomes():

        """Como acessar os nomes pelos índices"""
        for n in range(tamanho_lista):

            print(lista_pessoas[n])

        # Acessando os nomes por meio de seus índices. 
        print(lista_pessoas[-1])

        print("Primeiro Nome: ")
        print(lista_pessoas[0])

    def exibir_nomes(lista_nomes: List[str])-> None:

        tamanho_lista = len(lista_nomes)
        for n in range(tamanho_lista):
            print(lista_nomes[n])



    def trocando_nomes()-> None:

        tamanho_lista = len(lista_pessoas)

        print(f"Tamanho da lista: {tamanho_lista}")
        for n in range(tamanho_lista):
            lista_pessoas[n] = input("Indique um novo nome para alista: ")


        exibir_nomes(lista_nomes= lista_pessoas)

    # trocando_nomes() 


    def fatiando_lista()-> None:

        lista_nomes = ["Mateus", "Carlos", "Jonathas", "Davi", "Samuel"]

        def acessando_parte_lista()-> None:
            nomes_vistos = 0
            for nome in lista_nomes[:2]:
                print("Nome n°", nomes_vistos + 1, sep= "", end= "\n")
                print(nome)

                nomes_vistos += 1


        nomes_acessar = int(input("""Indique a quantidade 
de nomes que você pretende acessar:  """)) 

        for _ in range(nomes_acessar):

            indice = int(input("Indique o índice do nome que você quer acessar: "))

            try: 
                print(lista_nomes[indice])

            except IndexError as message:
                print(message)

                print("Tente encontrar um índice que esteja na lista.")

                time.sleep(2)

                print(f"Os índices estão entre 0 e {len(lista_nomes) - 1}.")
                time.sleep(2)
                print("Tentando novamente...")

                fatiando_lista()

    # fatiando_lista() 


    def imprimir_secoes_lista()-> None:

        """
            Imprimindo setores indicados da lista. 
            Por exemplo: Imprima do índice 2 até o índice quatro. 

        """

        lista_nomes = ["Marcos", "José", "Mateus", "Lucas"]


        while True:

            print("Para sair digite sair: ")

            opcao = input("Idique a sua opção: ").lower()

            if opcao == "sair":

                print("Saindo...")
                time.sleep(2)

            elif opcao == "imprimir":

                parte_a = int(input("Indique a primeira parte que você quer imprimir (pode ser um valor negativo): "))
                time.sleep(2)

                if parte_a < len(lista_nomes):

                    # Estou perguntando o índice do último valor que será impresso.  
                    parte_b = int(input("Indique a última parte "))

                


            else: 
                print("Opção inválida...")
                time.sleep(2)

                print("Tentando novamente...")
                time.sleep(2)



    # def 




def main():

    # manipulando_lista()

    minha_lista() 

    # trocando_nomes()


if __name__ == '__main__':
    main()