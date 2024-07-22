class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserirNoInicio(self, nodo):
        nodo.proximo = self.head
        self.head = nodo

    def imprimir(self):
        atual = self.head
        while atual:
            print(f"{atual.sigla} ({atual.nomeEstado})", end=" -> ")
            atual = atual.proximo
        print("None")

class TabelaHash:
    def __init__(self):
        self.tabela = [ListaEncadeada() for _ in range(10)]

    def funcaoHash(self, sigla):
        if sigla == "DF":
            return 7
        valor_ascii = ord(sigla[0]) + ord(sigla[1])
        return valor_ascii % 10

    def inserir(self, sigla, nomeEstado):
        nodo = Nodo(sigla, nomeEstado)
        indice = self.funcaoHash(sigla)
        self.tabela[indice].inserirNoInicio(nodo)

    def imprimirTabela(self):
        for i, lista in enumerate(self.tabela):
            print(f"Posição {i}: ", end="")
            lista.imprimir()

def inserirEstados(tabela):
    estados = {
        "AC": "Acre", "AL": "Alagoas", "AM": "Amazonas", "AP": "Amapá", "BA": "Bahia", "CE": "Ceará",
        "DF": "Distrito Federal", "ES": "Espírito Santo", "GO": "Goiás", "MA": "Maranhão", "MT": "Mato Grosso",
        "MS": "Mato Grosso do Sul", "MG": "Minas Gerais", "PA": "Pará", "PB": "Paraíba", "PR": "Paraná",
        "PE": "Pernambuco", "PI": "Piauí", "RJ": "Rio de Janeiro", "RN": "Rio Grande do Norte", "RS": "Rio Grande do Sul",
        "RO": "Rondônia", "RR": "Roraima", "SC": "Santa Catarina", "SP": "São Paulo", "SE": "Sergipe", "TO": "Tocantins"
    }
    for sigla, nome in estados.items():
        tabela.inserir(sigla, nome)

def inserirEstadoFicticio(tabela):
    estado_ficticio = "Estado Fictício"
    sigla_ficticia = "EF"
    tabela.inserir(sigla_ficticia, estado_ficticio)


def testar_sistema():
    tabela = TabelaHash()

    print("Tabela Hash antes de inserir qualquer informação:")
    tabela.imprimirTabela()

    
    inserirEstados(tabela)

    
    print("\nTabela Hash após inserir os 26 estados e o Distrito Federal:")
    tabela.imprimirTabela()

    
    inserirEstadoFicticio(tabela)

    
    print("\nTabela Hash após inserir os 26 estados, o Distrito Federal e o estado fictício:")
    tabela.imprimirTabela()

testar_sistema()

