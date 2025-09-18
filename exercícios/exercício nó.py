class No:
    def __init__(self, valor):
        self.valor = valor 
        self.proximo = None

    def mostraNo(self):
        print(self.valor)

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
    
    def insereInicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        if self.primeiro == None:
            print(f'A lista está vazia')
            return None
        atual = self.primeiro
        while atual != None:
            atual.mostraNo()
            atual = atual.proximo 


    def excluirInicio(self):
        if self.primeiro == None:
            print(f'A lista está vazia')
            return None
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp

    def pesquisa(self, valor):
        if self.primeiro == None:
            print (f'A lista está vazia')
            return None
        atual = self.primeiro
        while atual.valor != valor:
            if atual.valor == None:
                return None
            else:
                atual = atual.proximo
            return atual
        
    def excluirAleatorio(self, valor):
        if self.primeiro == None:
            print(f'A lista está vazia')
            return None
        atual = self.primeiro
        anterior = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                anterior = atual
                atual = atual.proximo
        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo
        return atual
    
#Início da Execução dos Passos
# a. Demonstrar a inserção de cada um dos caracteres que compõem seu primeiro nome;
meu_nome = "ALEXSANDER"
lista = ListaEncadeada()

print(f"Inserindo os caracteres do nome '{meu_nome}':")
for letra in meu_nome:
    lista.insereInicio(letra)
    print(f"Inserido: {letra}")

print("\n" + "="*40 + "\n")

# b. Demonstre a impressão de todos os elementos inseridos no item a;
print("Imprimindo todos os elementos da lista:")
# Nota: Como usamos insereInicio, a lista estará na ordem inversa.
lista.mostrar()

print("\n" + "="*40 + "\n")

# c. Faça a exclusão do primeiro elemento da lista;
print("Excluindo o primeiro elemento da lista.")
elemento_excluido_inicio = lista.excluirInicio()

print("\n" + "="*40 + "\n")

# d. Verifique se a operação executada no item c foi concluída;
print("Verificando a exclusão do primeiro elemento:")
if elemento_excluido_inicio is not None:
    print(f"Operação concluída. Elemento '{elemento_excluido_inicio.valor}' foi removido.")
    print("Estado atual da lista:")
    lista.mostrar()
else:
    print("A lista já estava vazia, nada foi removido.")

print("\n" + "="*40 + "\n")

# e. Faça a pesquisa pelo último caractere do seu nome. Qual o retorno do algoritmo?
ultimo_caractere = meu_nome[-1] # O último caractere é 'R'
print(f"Pesquisando pelo último caractere do nome ('{ultimo_caractere}'):")

resultado_pesquisa = lista.pesquisa(ultimo_caractere)

print("\n   Qual o retorno do algoritmo?")
if resultado_pesquisa is not None:
    print(f"   O algoritmo retornou o objeto Nó que contém o valor '{resultado_pesquisa.valor}'.")
else:
    print(f"   O algoritmo retornou 'None'.")
    print(f"   Isso ocorreu porque o caractere '{ultimo_caractere}' era o primeiro elemento da lista e foi removido no passo 'c'.")

print("\n" + "="*40 + "\n")

# f. Escolha um elemento qualquer (não pode ser o primeiro) e faça a sua exclusão.
elemento_para_excluir = 'S'
print(f"Excluindo um elemento que não é o primeiro (o caractere '{elemento_para_excluir}'):")
elemento_excluido_meio = lista.excluirAleatorio(elemento_para_excluir)

print("\n" + "="*40 + "\n")

# g. Verifique se a operação executada no item f foi concluída;
print("Verificando a exclusão do elemento escolhido:")
if elemento_excluido_meio is not None:
    print(f"   Operação concluída. Elemento '{elemento_excluido_meio.valor}' foi removido.")
    print("   Estado final da lista:")
    lista.mostrar()
else:
    print(f"   O elemento '{elemento_para_excluir}' não foi encontrado para exclusão.")