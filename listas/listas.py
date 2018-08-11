nomes = ['Erique','Rodrigo','Jose Julio','Diord','Guilherme','Jeferson','Vinicius']

saudacao = 'Ola Mano!'

print(nomes)

#adicionando um novo elemento na lista
nomes.append('Vandao')

print(nomes)

#criando uma lista vazia e adicionando elementos a listo 
#Com o comando append()
motocilcetas = []

msg = 'lista vazia', motocilcetas

#ate aqui a lista esta vazia
print(msg)

#agora vamos preenche-la
motocilcetas.append('honda')
motocilcetas.append('Yamaha')
motocilcetas.append('YBR')

print(motocilcetas)

#Usuando a função insert
#com essa função voce poderá inserir um valor em qualquer posição da lista
#informando o indice e o novo valor
motocilcetas.insert(1, 'Suzuki')

print(motocilcetas)

#Removendo elementos da lista
#A função del só pode ser usada se voce conhece a posição 
#Do elemento

#Aqui será removido o ultimo elemento da lista de nomes
del nomes[-1]
print(nomes)

#Removendo usando o comando pop()
#Com essa função voce pode remover e ainda ter acesso ao 
#item removido da lista
#essa função remove o ultimo elemento da lista
popped_motocicle = motocilcetas.pop()

print(motocilcetas)

#vamos mostrar o elemento removido
print(popped_motocicle)

