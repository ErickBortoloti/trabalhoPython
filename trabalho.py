class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserirSemPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            atual = self.head
            anterior = None
            while atual and atual.cor == 'A':
                anterior = atual
                atual = atual.proximo
            if anterior:
                nodo.proximo = anterior.proximo
                anterior.proximo = nodo
            else:
                nodo.proximo = self.head
                self.head = nodo

    def inserir(self):
        cor = input("Informe a cor do cartão (A ou V): ").upper()
        numero = int(input("Informe o número do cartão: "))
        novo_nodo = Nodo(numero, cor)
        if not self.head:
            self.head = novo_nodo
        else:
            if cor == 'V':
                self.inserirSemPrioridade(novo_nodo)
            elif cor == 'A':
                self.inserirComPrioridade(novo_nodo)

    def imprimirListaEspera(self):
        atual = self.head
        while atual:
            print(f"Cartão {atual.cor}{atual.numero}")
            atual = atual.proximo

    def atenderPaciente(self):
        if not self.head:
            print("Nenhum paciente na fila para atendimento.")
        else:
            print(f"Chamando paciente com cartão {self.head.cor}{self.head.numero} para atendimento.")
            self.head = self.head.proximo

def menu():
    lista = ListaEncadeada()
    while True:
        print("\nMenu:")
        print("1 – Adicionar paciente à fila")
        print("2 – Mostrar pacientes na fila")
        print("3 – Chamar paciente")
        print("4 – Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            lista.inserir()
        elif opcao == '2':
            lista.imprimirListaEspera()
        elif opcao == '3':
            lista.atenderPaciente()
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()

