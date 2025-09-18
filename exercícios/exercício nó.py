class No:
    def__innit__(self, valor):
        self.valor = valor 
        self.proximo = None

    def mostraNo(self):
        print(self.valor)

class ListaEncadeada:
    def__innit__(self):
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
        while atual.valor != self.valor:
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
            anterio