from faker import Faker 
from typing import List, Tuple
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


    # Adicionando elementos

    def adicionando_elementos()-> None:

        pessoas: List[Tuple[str, int]] = []

        while True:

            print("============ Opção ============")
            print("\nPara adicionar mais uma pessoa digite A")
            print("Para ver os nome adicionados digite V")
            print("Para sair digite S\n")

            opcao = input("Indique a sua opção: ").upper()

            if opcao == "A":

                print("Indique o nome: ")
                nome = input("").title()

                idade = int(input("Indique a idade: "))

                tupla_pessoa = (nome, idade)
                pessoas.append(tupla_pessoa)


            elif opcao == "V":

                for tupla_pessoa in pessoas: 

                    print(f"""
=========================
Nome: {tupla_pessoa[0]}
Idade: {tupla_pessoa[1]}\n""")                


            elif opcao == "S":

                print("Saindo...")
                time.sleep(2)

                # Criando um arquivo texto com os nomes salvos 

                print("Salvando nomes...")
                time.sleep(2)

                with open('estrutura_de_dados/salvar_nomes.txt', 'a') as file:
                    for tupla in pessoas:

                        texto = f"Nome: {tupla[0]}   idade: {tupla[1]}\n"
                        file.write(texto)

                break 

            else: 

                print("Opção não encontranda...")
                time.sleep(2)

                print("Tentando novamente...")
                time.sleep(2)




    # adicionando_elementos()

    def inserindo_elementos()-> None:

        lista_pessoa_a = ["Mateus", "Marcos", "João", "Lucas"]

        
        def mostrar_nome_indice(lista: List[str])-> None:
            for i in range(len(lista)):

                print("Indice:", i, "Nome:", lista[i])


        while True:

            print("Para inserir algum nome a um índice epecífico digite A.")
            print("Para ver a lista de nomes como os índices digite V.")
            print("Para sair digite S.")


            opcao = input("Indique a sua opção: ").lower()

            if opcao == "a": 

                # if len()

                indice = int(input("Indique o índice que você quer alterar: "))

                if indice < len(lista_pessoa_a):
                    
                    nome = input("Indique o nome que ocupará a lista nesta posição: ")
                    lista_pessoa_a.insert(indice, nome) 

                    print("Nome adicionado com sucesso!")
                    time.sleep(2)

                    print("...")
                    time.sleep(2)

    def removendo_elementos():

        lista_a = ["Marcos", "João", "Jonathas"]

        return lista_a.pop()

    removendo_elementos()
def main():

    # manipulando_lista()

    # minha_lista() 

    # trocando_nomes()

    print(f"Elemento removido: {minha_lista()}")



if __name__ == '__main__':
    main()