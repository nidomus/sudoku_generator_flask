from quadrante import Quadrante, BlockedException
from random import randint


class Sudoku():
    def __init__(self) -> None:
        # Inicializa os quadrantes do tabuleiro
        quadrante_1 = Quadrante(0)
        quadrante_2 = Quadrante(1)
        quadrante_3 = Quadrante(2)
        quadrante_4 = Quadrante(3)
        quadrante_5 = Quadrante(4)
        quadrante_6 = Quadrante(5)
        quadrante_7 = Quadrante(6)
        quadrante_8 = Quadrante(7)
        quadrante_9 = Quadrante(8)

        quadrante_1.set_vizinhos_h([quadrante_2, quadrante_3])
        quadrante_1.set_vizinhos_v([quadrante_4, quadrante_7])

        quadrante_2.set_vizinhos_h([quadrante_1, quadrante_3])
        quadrante_2.set_vizinhos_v([quadrante_5, quadrante_8])

        quadrante_3.set_vizinhos_h([quadrante_1, quadrante_2])
        quadrante_3.set_vizinhos_v([quadrante_6, quadrante_9])

        quadrante_4.set_vizinhos_h([quadrante_5, quadrante_6])
        quadrante_4.set_vizinhos_v([quadrante_1, quadrante_7])

        quadrante_5.set_vizinhos_h([quadrante_4, quadrante_6])
        quadrante_5.set_vizinhos_v([quadrante_2, quadrante_8])

        quadrante_6.set_vizinhos_h([quadrante_4, quadrante_5])
        quadrante_6.set_vizinhos_v([quadrante_3, quadrante_9])

        quadrante_7.set_vizinhos_h([quadrante_8, quadrante_9])
        quadrante_7.set_vizinhos_v([quadrante_1, quadrante_4])

        quadrante_8.set_vizinhos_h([quadrante_7, quadrante_9])
        quadrante_8.set_vizinhos_v([quadrante_2, quadrante_5])

        quadrante_9.set_vizinhos_h([quadrante_7, quadrante_8])
        quadrante_9.set_vizinhos_v([quadrante_3, quadrante_6])

        self.quadrantes: list[Quadrante] = [quadrante_1, quadrante_2, quadrante_3,
                                            quadrante_4, quadrante_5, quadrante_6, quadrante_7, quadrante_8, quadrante_9]

        self.quadrantes_copia = []
        self.resolvido = False
        self.solucao = None
        self.preencher_tabuleiro()

    def preencher_tabuleiro(self):

        # Preenche todas as casas do tabuleiro
        flag = False
        while flag == False:
            flag = True
            for quadrante in self.quadrantes:
                try:
                    quadrante.preencher_matriz()
                except BlockedException:
                    self.zerar_quadrantes()
                    flag = False

    def verificar_tabuleiro(self, lista=None):
        if not lista:
            lista = self.quadrantes

        for quadrante in self.quadrantes:
            self.matriz = quadrante.matriz

            for i in range(3):
                for j in range(3):
                    if quadrante.verificar_vizinhos(self.matriz[i][j], i, j):
                        return False
        return True

    def gerar_jogo(self):

        espacos_vazios = 0
        while espacos_vazios <= 46:

            quad = randint(0, 8)
            i = randint(0, 2)
            j = randint(0, 2)
            # and (self.quadrantes[quad].quantidade_valor(0) < 9)
            if self.quadrantes[quad].matriz[i][j] != 0 and (self.quadrantes[quad].quantidade_valor(0) < 8):
                self.quadrantes[quad].matriz[i][j] = 0
                espacos_vazios += 1

    def encontrar_valores_invalidos(self, quad, valor, linha, coluna):

        coordenadas = []

        for i in range(3):
            for j in range(3):
                if self.quadrantes[quad].matriz[i][j] == valor and not (i == linha and j == coluna):
                    coordenadas.append((quad, i, j))

        for vizinho in self.quadrantes[quad].vizinhos_h:
            aux = vizinho.verificar_linha(valor, linha)
            if aux is not None:
                coordenadas.append(aux)

        for vizinho in self.quadrantes[quad].vizinhos_v:
            aux = vizinho.verificar_coluna(valor, coluna)
            if aux is not None:
                coordenadas.append(aux)
        return coordenadas

    def converte_coordenada_local(self, quad, valor):

        for linha in range(9):
            if valor in self.mapa[linha]:
                coluna = self.mapa[linha].index(valor)
                break

        if linha < 3:
            i = linha
        else:
            i = linha % 3

        if coluna < 3:
            j = coluna
        else:
            j = coluna % 3

        return i, j

    def zerar_quadrantes(self):
        for quadrante in self.quadrantes:
            quadrante.matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def gerar_mapa(self):
        x = [[], [], [], [], [], [], [], [], []]
        for i in range(9):
            for j in range(9):
                x[i].append(j+(i*9))
        return x

    def print_tabuleiro(self):
        print('-'*31)
        for i in range(3):
            print(self.quadrantes[0].matriz[i], end='  ')
            print(self.quadrantes[1].matriz[i], end='  ')
            print(self.quadrantes[2].matriz[i], end='  ')
            print()

        print()

        for i in range(3):
            print(self.quadrantes[3].matriz[i], end='  ')
            print(self.quadrantes[4].matriz[i], end='  ')
            print(self.quadrantes[5].matriz[i], end='  ')
            print()

        print()

        for i in range(3):
            print(self.quadrantes[6].matriz[i], end='  ')
            print(self.quadrantes[7].matriz[i], end='  ')
            print(self.quadrantes[8].matriz[i], end='  ')
            print()
        print()

    def get_json_tabuleiro(self):

        json = {"data": []}

        intervalo = 0
        while intervalo < 9:
            intervalo += 3
            for i in range(3):
                for j in range(intervalo-3, intervalo):
                    for k in range(0, 3):

                        row, column = self.quadrantes[j].coordenada_absoluta(
                            i, k)

                        number = {

                            "number": self.quadrantes[j].matriz[i][k],
                            "row":  i,
                            "column": column,
                            "quadrant": self.quadrantes[j].numero

                        }

                        json['data'].append(number)

        return json
