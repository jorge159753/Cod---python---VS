#Criando os marcadores e ponteiros da lista Simples
class Node:

    def __init__(self, data):
        self.data = data #Conteúdo armazenado no nó.
        self.next = None #Iniciar o proximo valor da Array como nulo

#Criando a lista_Simples
class simple_list:

    def __init__(self):
        self.header = None #Construtor da lista

    #Criando o metodo de adicionar no inicio
    def append_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.header
        self.header = new_node

    def append_at_end(self, data):
        new_node = Node(data) #Adicionando o novo 'Nó' no fim da lista

        #Caso a lista estaja vazia, irar adicionar o primero elemento da Array como ser o novo_node

        if self.header == None:
            self.header = new_node
            return
        
        atual_node = self.header #Irá classificar o nó atual na array
        while atual_node.next:  #Percorre toda a Array
            atual_node = atual_node.next

        atual_node.next = new_node #Muda o 'nó' atual
        return
    
    #Criando o metodo de Adicionar em qualquer posição
    def append_at_index(self, data, index):

        #Condição para caso a lista esteja vazia
        if index == 1:
            new_node = Node(data)
            new_node.next = self.header
            self.header = new_node


        i = 1
        atual_node = self.header
        while i < index - 1 and atual_node is not None:
            atual_node = atual_node.next
            i = i + 1 #Percorre a lista até chegar na posição onde o nó é inserido

        if atual_node is None:
            print("ERRO: posição não encontrada!")
        else:
            new_node = Node(data)
            new_node.next = atual_node.next
            atual_node.next = new_node

    #Criando o metodo de remover o elemento da lista no inicio
    def remove_at_start(self):

        #Caso a lista esteja vazia
        if self.header == None:
            print("Essa lista não tem elementos!")
            return
        self.header = self.header.next

    #Remover no fim da Array
    def remove_at_end(self):
        if self.header == None:
            print("Essa lista não tem elementos!")
            return
        atual_node = self.header

        while atual_node.next.next != None:
            atual_node = atual_node.next
        
        atual_node.next = None

    #Remover por posição
    def remove_at_index(self, index):
        if self.header == None:
            print("Essa lista não tem elementos!")
            return
        atual_node = self.header

        i = 1
        while i < index - 1:
            atual_node = atual_node.next
            i += 1

        if atual_node is None or atual_node.next is None:
            print("ERRO: Indice fora dos limites ou lista está vazia!")

        #Removendo o elemento definido e realocando outro no lugar
        next_node = atual_node.next.next
        atual_node.next = next_node

    #Retorna o tamanho da lista simples
    def len(self):

        #Verifica se a lista está vazia
        if self.header == None:
            return 0
        
        #Caso a lista esteja vazia, irá indicar que ela não possui elementos
        atual_node = self.header
        total = 0

        #Percorrerá a lista caso tenha elementos nela
        while atual_node:
            total += 1 #Contará o tamanho da lista

            atual_node = atual_node.next
        return total #Tamanho da lista

    #Converter a lista simples para uma lista em Python
    def to_list(self):

        node_data = [] #Vetor vazio
        atual_node = self.header

        while atual_node: 
            node_data.append(atual_node.data) #Adiciona o dado armazenado no Vetor
            atual_node = atual_node.next #Busca o proximo dado na Array
        return node_data
    
    #Retorna o tamanho da lista
    def length(self):
        if self.header == None:
            return 0
        atual_node = self.header
        total = 0

        while atual_node:
            atual_node = atual_node.next
            total += 1
        return total


    def get(self, index):

        if index >= self.length() or index < 0:
            print("ERRO: 'Obter' posição inválida!" )
            return None
        

        atual_idx = 0
        atual_node = self.header
        while atual_node != None: 
            if atual_idx == index: 
                return atual_node.data
            atual_node = atual_node.next
            atual_idx += 1
        return atual_idx

    def display(self):
        contents = self.header

        #Se a lista estiver vazia
        if contents is None:
            print("Nenhum elemento encontrado!")
            return
        
        while contents:
            print(contents.data)
            contents = contents.next
        
        print("----------")