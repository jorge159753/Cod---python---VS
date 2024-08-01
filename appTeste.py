from appEstrutura import *

#testes

my_list = simple_list()


my_list.append(3)
my_list.append(2)
my_list.append(7)
my_list.append(1)

print("Tamanho da lista:")
print(my_list.len())
print("\n")

print("Lista no modelo python:")
lista_python = my_list.to_list()
print(lista_python)
print('\n')

print("Adicionar no inicio da lista:")
my_list.append_at_start(8)
my_list.display()
print('\n')

print("Adicionar na posição desejada:")
my_list.append_at_index(6, 5)
my_list.display()
print('\n')

print("Adicionar no fim da lista:")
my_list.append(10)
my_list.display()
print('\n')

print("Remover do inicio:")
my_list.remove_at_start()
my_list.display()
print('\n')

print("Remover posição desejada:")
my_list.remove_at_index(3)
my_list.display()
print('\n')

print("Remover do final da lista:")
my_list.remove_at_end()
my_list.display()
print('\n')

print("Mostrar um elemento de determinada posição:")
my_list.get(1)
my_list.display()
print('\n')

print("Tamanho da lista:")
print(my_list.len())
print("\n")

print("Lista no modelo python:")
lista_python = my_list.to_list()
print(lista_python)
print("----------")