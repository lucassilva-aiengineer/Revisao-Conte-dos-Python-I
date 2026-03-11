# Strings 

# Um tipo de dados ordenado em imutável utilizado na representação
# de texto, na prática, cadeia de carcteres. 

minha_string = "Meu nome é Marcos."


minha_string = "Maça"

caracter = minha_string[0]

# print(minha_string)
# print(caracter)

# Fatiando uma string 
substring = minha_string[2: 5]
# print(substring)

copia_a = minha_string[:]
# print(copia_a)

profissao = "Engenharia"

substring_3 = minha_string[::2]

# print(substring_3)

minha_string_4 = profissao[::2] # Indo do primeiro ao último índice 
                                # Saltando de dois em dois itens. 

# Concatenando 
# Juntando strings. 

nome = "Marcos"
sobrenome = "Johan"
nome_completo = nome + " " + sobrenome 

# print(nome_completo)

# Iterando uma string 

for item in "Nome Pessoa":
    print(item)


nome = "Marcos"
if "o" in nome:
    print("Nome possui a letra o.")


# Os métodos de 


# print(minha_string_4)